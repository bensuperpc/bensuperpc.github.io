+++
title = "C++ Code Coverage with CMake and GCOVR"
description = "This tutorial shows how to set up a C++ project with CMake and GCOVR to generate code coverage reports."
date = 2025-08-07T00:00:00Z
draft = false
aliases = ["en/tutorials/code-coverage"]

[taxonomies]
tags = ["Features","Code coverage", "Testing", "GCOVR"]
categories = ["Software"]
[extra]
keywords = "coverage, GCOVR, code coverage, testing, software quality"
toc = true
series = "Features"
+++

# Code Coverage in C/C++ with CMake and GCOVR

## Introduction

This tutorial shows how to set up a C/C++ project with CMake and GCOVR to generate code coverage reports, this allows you to precisely verify which parts of the source code and which conditional branches (if, switch, etc.) are actually covered by the tests.

We’ll use a small sample project based on Google Test, but the method is also compatible with other frameworks such as Catch2, Boost.Test, or Doctest.

## Minimum Requirements

- CMake 3.15
- GCC or Clang (C++17)
- Google Test (GTest)
- GCOVR 5.0
- Ninja (optional, but recommended)

A distribution like **Ubuntu 22.04**, **Debian 12** or higher is recommended for this tutorial, but you can use any Linux distribution with the required versions of the tools.


### Installing Dependencies

To install the necessary dependencies, you can use the following commands:

For **Ubuntu/Debian** :

```bash
sudo apt-get install cmake build-essential g++ gcovr ninja-build libgtest-dev
```

For **Fedora** :

```bash
sudo dnf install cmake gcc-c++ gcovr ninja-build gtest-devel
```

For **Arch Linux** :

```bash
sudo pacman -S cmake gcc gcovr ninja gtest
```

## What is GCOVR?

GCOVR is an open-source tool that generates C/C++ code coverage reports from the data produced during test execution.

## Sample Project

The sample project is a simple application and two C++ libraries, one for mathematics and one for physics.

Here is the project structure:

```bash
.
├── CMakeLists.txt
├── main.cpp
├── math
│   ├── CMakeLists.txt
│   ├── math.cpp
│   └── math.hpp
├── physics
│   ├── CMakeLists.txt
│   ├── physics.cpp
│   └── physics.hpp
└── tests
    ├── CMakeLists.txt
    └── test.cpp

4 directories, 10 files
```

You can **download** the sample project: {{ static_link(label="tuto_coverage.7z", file="/posts/tutorials/coverage/sources/tuto_coverage.7z") }}

### Compilation with Coverage

To enable code coverage, the project must be compiled with the options: `-O0 -g3 --coverage` and `--coverage` for linking.

```bash
cmake -S . -B build -G Ninja -DCMAKE_CXX_FLAGS="-O0 -g3 --coverage" -DCMAKE_EXE_LINKER_FLAGS="--coverage" && cmake --build build
```

The `--coverage` option is equivalent to `-fprofile-arcs -ftest-coverage` for GCC/Clang, in a classic project, it is preferable to use CMake presets rather than specifying the options manually.

The `-O0` and `-g3` options are used to disable optimizations and include debugging information for accurate code coverage.

### Running Tests

Once the project is compiled, you can run the tests, this will generate files on which GCOVR relies to generate coverage reports:

- `.gcno` generated at compile time, contains metadata for coverage
- `.gcda` generated at runtime, contains the collected coverage data


```bash
ctest --test-dir build --output-on-failure --no-tests=error --repeat until-fail:1 --schedule-random --parallel 1
```

|         Option          |                      Description                      |
| :---------------------: | :---------------------------------------------------: |
|   `--test-dir build`    |      Specify the directory containing the tests       |
|  `--output-on-failure`  |            Show the output of failed tests            |
|   `--no-tests=error`    |       Generates an error if no tests are found        |
| `--repeat until-fail:1` | Repeats the tests until a failure occurs, here 1 time |
|   `--schedule-random`   |            Runs the tests in random order             |
|     `--parallel 1`      |   Runs the tests in parallel, here 1 test at a time   |

You will get output similar to:

```bash
Test project /home/bensuperpc/tuto_coverage/build
    Start 3: MathTests.Mul
1/7 Test #3: MathTests.Mul .....................   Passed    0.00 sec
    Start 7: PhysicsTests.GravitationalForce
2/7 Test #7: PhysicsTests.GravitationalForce ...   Passed    0.00 sec
    Start 5: PhysicsTests.Speed
3/7 Test #5: PhysicsTests.Speed ................   Passed    0.00 sec
    Start 2: MathTests.Sub
4/7 Test #2: MathTests.Sub .....................   Passed    0.00 sec
    Start 1: MathTests.Add
5/7 Test #1: MathTests.Add .....................   Passed    0.00 sec
    Start 6: PhysicsTests.KineticEnergy
6/7 Test #6: PhysicsTests.KineticEnergy ........   Passed    0.00 sec
    Start 4: MathTests.Div
7/7 Test #4: MathTests.Div .....................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 7

Total Test time (real) =   0.02 sec
```

### HTML Report with GCOVR

After running the tests, you can generate a coverage report with GCOVR, here we generate an HTML report to visualize the code coverage, but you can also generate reports in plain text, XML or JSON.

```bash
gcovr --root . --decisions --calls --html-theme "green" --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --html --html-details --output "build/coverage.html"
```

|              Option              |                    Description                     |
| :------------------------------: | :------------------------------------------------: |
|            `--root .`            |        Sets the root directory for coverage        |
|          `--decisions`           |     Includes coverage decisions in the report      |
|            `--calls`             |       Includes function calls in the report        |
|      `--html-theme "green"`      |        Sets the HTML report theme to green         |
|      `--exclude "tests/*"`       |        Excludes test files from the report         |
|      `--exclude "build/*"`       |        Excludes build files from the report        |
|      `--exclude "main.cpp"`      |    Excludes the `main.cpp` file from the report    |
|             `--html`             |              Generates an HTML report              |
|         `--html-details`         |        Includes details in the HTML report         |
| `--output "build/coverage.html"` | Specifies the output file name for the HTML report |

GCovr will generate up to 5 files in the build folder:

- `coverage.html`: Main HTML report
- `coverage.css`: CSS file for styling the HTML report
- `coverage.functions.html`: Report showing the number of calls per function
- `coverage.math.cpp.xxxxxxx.html`: Coverage report for the math.cpp file
- `coverage.physics.cpp.xxxxxxx.html`: Coverage report for the physics.cpp file

You can open `build/coverage.html` in your browser to view the overall code coverage, and then explore each source file in more detail.

Here is the rendering of the report in the browser:

{{ img(src="/posts/tutorials/coverage/images/Screenshot_20250807_100908.webp" class="b1" alt="GCovr code coverage report by file" caption="GCovr code coverage report by file" link="") }}

{{ img(src="/posts/tutorials/coverage/images/Screenshot_20250807_101010.webp" class="b1" alt="Secondary Page" caption="Secondary Page" link="") }}

#### XML or JSON Report

You can also generate a report in XML or JSON for integration with other tools:

```bash
gcovr --root . --decisions --calls --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --xml-pretty --output "build/coverage.xml"
```

Or in JSON :

```bash
gcovr --root . --decisions --calls --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --json-pretty --output "build/coverage.json"
```

### CI/CD Integration

You can integrate coverage report generation into your CI/CD pipelines using GitHub Actions, GitLab CI/CD, or Jenkins.

Here’s an example configuration for GitLab CI/CD:

```yaml
variables:
  MINIMUM_LINE_COVERAGE: 67
  MINIMUM_FUNCTION_COVERAGE: 55
  MINIMUM_BRANCH_COVERAGE: 20

stages:
  - coverage

coverage-generic:
    stage: coverage
    image: gcc:latest
    script:
        - apt-get update && apt-get install -y cmake build-essential g++ gcovr ninja-build libgtest-dev
        - cmake -S . -B build -G Ninja -DCMAKE_CXX_FLAGS="-O0 -g3 --coverage" -DCMAKE_EXE_LINKER_FLAGS="--coverage"
        - cmake --build build
        - ctest --test-dir build --output-on-failure --no-tests=error --repeat until-fail:1 --schedule-random --parallel 1
        - gcovr --root . --decisions --calls --html-theme "green" --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --html --html-details --output "build/coverage.html"
        - gcovr --root . --decisions --calls --html-theme "green" --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --xml-pretty -o "build/coverage.xml"
        - gcovr --root . --decisions --calls --print-summary --fail-under-line $MINIMUM_LINE_COVERAGE --fail-under-function $MINIMUM_FUNCTION_COVERAGE --fail-under-branch $MINIMUM_BRANCH_COVERAGE
    artifacts:
        when: always
        paths:
        - build/*.html
        - build/*.css
        - build/*.xml
        coverage: '/^TOTAL.*\s+(\d+\%)$/'
```

## Sources

- [GCOVR](https://gcovr.com/en/latest/)
- [Google Test](https://github.com/google/googletest)
