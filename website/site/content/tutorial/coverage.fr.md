+++
title = "Couverture de code C++ avec CMake et GCOVR"
description = "Ce tutoriel montre comment configurer un projet C++ avec CMake et GCOVR pour générer des rapports de couverture de code."
date = 2025-08-07T00:00:00Z
draft = false
aliases = ["fr/tutorial/code-coverage"]

[taxonomies]
tags = ["Features","Code coverage", "Testing", "GCOVR"]
categories = ["Software"]
[extra]
keywords = "coverage, GCOVR, code coverage, testing, software quality"
toc = true
series = "Features"
+++

# Couverture de code en C/C++, avec CMake et GCOVR

## Introduction

Ce tutoriel montre comment configurer un projet C/C++ avec CMake et GCOVR afin de générer des rapports de couverture de code, cela permet de vérifier précisément quelles parties du code source et quelles branches conditionnelles (if, switch...) sont effectivement couvertes par les tests.

Nous utiliserons un petit projet d'exemple basé sur Google Test, mais la méthode est également compatible avec d'autres frameworks comme **Catch2**, **Boost.Test** ou **Doctest**.

## Exigences minimales

- CMake 3.15
- GCC ou Clang (C++17)
- Google Test (GTest)
- GCOVR 5.0
- Ninja (optionnel, mais recommandé)

Une distribution comme **Ubuntu 22.04**, un **Debian 12** ou supérieur est recommandé dans le cadre de ce tutoriel, mais vous pouvez utiliser n'importe quelle distribution Linux avec les versions requises des outils.


### Installation des dépendances

Pour installer les dépendances nécessaires, vous pouvez utiliser les commandes suivantes :

Pour **Ubuntu/Debian** :

```bash
sudo apt-get install cmake build-essential g++ gcovr ninja-build libgtest-dev
```

Pour **Fedora** :

```bash
sudo dnf install cmake gcc-c++ gcovr ninja-build gtest-devel
```

Pour **Arch Linux** :

```bash
sudo pacman -S cmake gcc gcovr ninja gtest
```

## Qu'est-ce que GCOVR ?

GCOVR est un outil open source qui permet de générer des rapports de couverture de code C/C++ à partir des données générées lors de l'exécution des tests.

## Projet d'exemple

Le projet d'exemple est une simple application et deux bibliothèques C++, une pour les mathématiques et une pour la physique. 

Voici l’arborescence du projet :

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

Vous pouvez télécharger le projet d'exemple: {{ static_link(label="tuto_coverage.7z", file="/tutorial/sources/tuto_coverage.7z") }}

### Compilation avec couverture

Pour que la couverture de code fonctionne, le projet doit être compilé avec les options : `-O0 -g --coverage` et `--coverage` pour le linkage.

```bash
cmake -S . -B build -G Ninja -DCMAKE_CXX_FLAGS="-O0 -g --coverage" -DCMAKE_EXE_LINKER_FLAGS="--coverage" && cmake --build build
```

L'option `--coverage` est équivalente à `-fprofile-arcs -ftest-coverage` pour GCC/Clang, dans un projet classique, il est préférable d'utiliser des presets CMake plutôt que de spécifier les options manuellement.

### Exécution des tests

Une fois le projet compilé, vous pouvez exécuter les tests, cela générera des fichiers sur lesquels GCOVR s’appuie pour générer les rapports de couverture:

- `.gcno` généré à la compilation, contient les métadonnées pour la couverture
- `.gcda` généré à l'exécution, contient les données de couverture collectées


```bash
ctest --test-dir build --output-on-failure --no-tests=error --repeat until-fail:1 --schedule-random --parallel 1
```

|         Option          |                           Description                           |
| :---------------------: | :-------------------------------------------------------------: |
|   `--test-dir build`    |           Spécifie le Répertoire contenant les tests            |
|  `--output-on-failure`  |               Affiche la sortie des tests échoués               |
|   `--no-tests=error`    |          Génère une erreur si aucun test n'est trouvé           |
| `--repeat until-fail:1` | Répète les tests jusqu'à ce qu'un échec se produise, ici 1 fois |
|   `--schedule-random`   |         Fait exécuter les tests dans un ordre aléatoire         |
|     `--parallel 1`      |      Exécute les tests en parallèle, ici 1 test à la fois       |

Vous obtiendrez une sortie similaire à :

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

### Rapport HTML avec GCOVR

Après l'exécution des tests, vous pouvez générer un rapport de couverture avec GCOVR, ici nous générons un rapport HTML pour visualiser la couverture de code, mais vous pouvez également générer des rapports en texte brut, XML ou JSON.

```bash
gcovr --root "." --decisions --calls --html-theme "green" --exclude "tests/*" --exclude "build/*" --exclude "main.cpp" --html --html-details --output "build/coverage.html"
```

|              Option              |                        Description                        |
| :------------------------------: | :-------------------------------------------------------: |
|           `--root "."`           |      Définit le répertoire racine pour la couverture      |
|          `--decisions`           |    Inclut les décisions de couverture dans le rapport     |
|            `--calls`             |       Inclut les appels de fonction dans le rapport       |
|      `--html-theme "green"`      |         Définit le thème du rapport HTML en vert          |
|      `--exclude "tests/*"`       |          Exclut les fichiers de test du rapport           |
|      `--exclude "build/*"`       |          Exclut les fichiers de build du rapport          |
|      `--exclude "main.cpp"`      |          Exclut le fichier `main.cpp` du rapport          |
|             `--html`             |                  Génère un rapport HTML                   |
|         `--html-details`         |          Inclut les détails dans le rapport HTML          |
| `--output "build/coverage.html"` | Spécifie le nom du fichier de sortie pour le rapport HTML |

Une fois le rapport HTML généré, vous pouvez l'ouvrir dans votre navigateur pour visualiser la couverture de code, il devrait être généré dans le fichier `build/coverage.html`.

Voici le rendu du rapport sur le navigateur :

{{ img(src="/tutorial/images/Screenshot_20250807_100908.webp" class="b1" alt="Page principale" caption="Page principale" link="") }}

{{ img(src="/tutorial/images/Screenshot_20250807_101010.webp" class="b1" alt="Page secondaire" caption="Page secondaire" link="") }}

#### Rapport en XML ou JSON

Vous pouvez également générer un rapport en XML ou JSON pour une intégration avec d'autres outils :

```bash
gcovr --root "." --decisions --calls --exclude "tests/" --exclude "build/" --exclude "main.cpp" --xml-pretty --output "build/coverage.xml"
```

Or in JSON :

```bash
gcovr --root "." --decisions --calls --exclude "tests/" --exclude "build/" --exclude "main.cpp" --json-pretty --output "build/coverage.json"
```

## CI/CD Integration

Vous pouvez intégrer la génération de couverture de code à votre pipeline CI/CD afin de générer automatiquement des rapports pour chaque commit ou demande de fusion.

Voici un exemple de GitLab CI pour générer un rapport de couverture et fail le pipeline si la couverture est inférieure à un certains seuils:

```yaml
variables:
  # Si quelqu'un oublie d'ajouter des tests sur une nouvelle fonctionnalité, le pipeline échouera si la couverture est inférieure à ces seuils
  MIN_LINE_COVERAGE: 50
  MIN_FUNCTION_COVERAGE: 50
  MIN_BRANCH_COVERAGE: 50
  MIN_DECISION_COVERAGE: 50

stages:
  - coverage

coverage_stage:
  stage: coverage
  script:
    # Compiler le projet avec les flags de couverture
    - cmake -S . -B build -G Ninja -DCMAKE_CXX_FLAGS="-O0 -g --coverage" -DCMAKE_EXE_LINKER_FLAGS="--coverage" && cmake --build build
    # Exécuter les tests pour générer les données de couverture
    - ctest --verbose --repeat until-fail:1 --parallel 1 --schedule-random --test-dir build || true
    # Créer le répertoire pour les rapports de couverture HTML
    - mkdir -p "coverage_html_$CI_COMMIT_SHORT_SHA"
    # Générer les rapports de couverture HTML
    - gcovr --root "." --exclude "tests/" --exclude "build/" --exclude "main.cpp" --decisions --calls --html --html-theme green --html-details -o "coverage_html_$CI_COMMIT_SHORT_SHA/coverage.html"
    # Générer le rapport de couverture XML (pour Gitlab)
    - gcovr --root "." --exclude "tests/" --exclude "build/" --exclude "main.cpp" --decisions --calls --xml-pretty -o coverage.xml
    # Vérifier les seuils minimum de couverture
    - gcovr --root "." --exclude "tests/" --exclude "build/" --exclude "main.cpp" --decisions --calls --print-summary --fail-under-line $MIN_LINE_COVERAGE --fail-under-branch $MIN_BRANCH_COVERAGE --fail-under-function $MIN_FUNCTION_COVERAGE --fail-under-decision $MIN_DECISION_COVERAGE
  artifacts:
    name: "$CI_PROJECT_NAME-$CI_COMMIT_SHORT_SHA"
    expire_in: 7 days
    when: always
    paths:
      - "coverage_html_$CI_COMMIT_SHORT_SHA/*"
      - "coverage.xml"
  # Parser le coverage depuis le fichier coverage.xml
  coverage: '/lines: (\d+\.\d+)%/'
```



## Sources

- [GCOVR](https://gcovr.com/en/latest/)
- [Google Test](https://github.com/google/googletest)
