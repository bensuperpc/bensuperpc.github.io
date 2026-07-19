+++
title = "Guide des PC SFF (WIP)"
description = "Un guide des PC SFF"
date = 2025-12-27T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","SFF","Tiny","Thinkcentre"]
categories = ["Hardware"]
[extra]
keywords = "SFF, Tiny, Embed, Embedded, Streamable"
toc = true
series = "Features"
+++

# Guide des PC SFF

Bienvenue dans le guide des PC SFF.

## Introduction aux PC SFF

Dans cette section, nous allons explorer différents aspects des PC SFF, notamment leurs composants et leurs logiciels, en mettant l'accent sur les solutions **Linux** et **open-source**, Windows a souvent un support à plus court et repose sur des logiciels propriétaires.

### Qu'est-ce qu'un PC SFF ?

Un PC SFF (**PC Small Form Factor**) est un ordinateur de bureau de petite taille (1 à 5 litres), souvent très économe en énergie, et peut servir à divers usages, on les trouve couramment dans les écoles, les bureaux et comme serveurs.

### Pourquoi choisir un PC SFF ?

Il existe de nombreuses raisons de choisir un PC SFF :

- **Compact** : les PC SFF sont très petits et peuvent tenir presque n'importe où (~1 à 5 litres).
- **Économe en énergie** : ils consomment souvent moins d'énergie, en particulier les modèles équipés de processeurs des séries T ou U.
- **Abordable** : les PC SFF sont souvent moins chers que les PC de bureau classiques, surtout sur le marché de l'occasion.

### Pourquoi ne pas choisir un PC SFF ?

Il y a aussi quelques inconvénients à prendre en compte :

- **Évolutivité limitée** : Les PC SFF offrent peu d'options d'évolution, voire même certains composants ne sont pas remplaçables.
- **Moins de ports** : Par rapport aux ordinateurs de bureau classiques, les PC SFF disposent généralement de moins d'options de connectique (USB, HDMI, DisplayPort, etc.).
- **Performances contraintes** : En raison de leur petite taille et de leurs limites thermiques, les performances peuvent être inférieures à celles des PC de taille standard.
- **Composants propriétaires** : Certains modèles utilisent des pièces propriétaires, ce qui rend les réparations et les mises à niveau plus difficiles.

### Quels sont quelques exemples de PC SFF ?

Voici quelques marques et modèles de PC SFF populaires :

- **Lenovo ThinkCentre** : M73 Tiny, M710q, M720q, M70q gen 1, M75q gen 1, M90q gen 3
- **Dell OptiPlex** : 3040, 3050, 3060, 3070, 5040, 5050, 5060, 5070
- **HP EliteDesk** : 800 G1 Mini, 800 G2 Mini
- **Intel NUC** : NUC6i3SYH, NUC6i5SYH, NUC6i7KYK, NUC7i3BNH, NUC7i5BNH, NUC7i7BNH
- **Zotac ZBOX** : CI660 Nano, CI640 Nano, CI620 Nano, CI540 Nano, CI520 Nano, CI327 Nano
- **Asus VivoMini** : UN65, UN65U, UN65U-M023M, UN65U-M021M, UN65U-M022M, UN65U-M020M

De nombreuses autres marques et modèles sont disponibles sur le marché.

Pour l'occasion, je recommande **Lenovo, Dell et HP**, ces marques se trouvent régulièrement en grande quantité sur le marché de l'occasion, souvent évolutifs (RAM, SSD, CPU, PSU) et offrant une bonne compatibilité avec Linux.

### Les PC SFF ARM

Les PC SFF sont généralement basés sur x86, mais les PC SFF basés sur ARM gagnent en popularité ces dernières années, ils sont généralement moins chers et plus économes en énergie, mais présentent certaines limites :

- **Compatibilité logicielle limitée** : ils ne sont pas compatibles avec les logiciels x86/PC traditionnels, et les pilotes peuvent être manquants ou obsolètes.
- **Options d'évolution limitées** : les composants sont souvent soudés et non remplaçables.
- **Performances inférieures** : par rapport à leurs équivalents x86, les PC SFF basés sur ARM sont souvent moins performants.

Dans ce guide, nous nous concentrerons sur les PC SFF x86 et le Raspberry Pi.

## Composants des PC SFF

Dans cette section, nous allons examiner les principaux composants des PC SFF.

### CPU (Central Processing Unit)

Je recommande d'utiliser des **CPU sur socket**, car ils permettent de futures mises à niveau vers des modèles plus puissants (dans la même plage de TDP), par exemple, sur un ThinkCentre Tiny M720q, vous pouvez passer d'un **Intel Celeron G4900T** à un **Intel i9-9900T** sans aucun problème (il faut parfois seulement mettre à jour l'Intel ME et le BIOS).

La plupart des PC SFF sont livrés avec des **CPU de 35 W ou 65 W**, **Je recommande fortement d'éviter les CPU dont le TDP est supérieur à ce que le système prend en charge**, car cela peut provoquer une surchauffe et potentiellement endommager la carte mère ou le PSU.

De nombreux logiciels modernes utilisent les instructions **AVX2**, qui peuvent améliorer considérablement les performances dans des tâches comme l'encodage/décodage vidéo, la compression, le chiffrement, etc, tous les CPU depuis **Intel Haswell** (2013) et **AMD Zen** (2017) prennent en charge AVX2, à l'exception de certains modèles d'entrée de gamme comme les **Intel Celeron/Pentium/Atom** et les **AMD Athlon**.

#### Générations de CPU Intel

| Marque | Arch. CPU    | Gén. CPU    | Socket  | Type de RAM | RAM max | Année     | Exemple de PC SFF | Remarques                                                       |
| ------ | ------------ | ----------- | ------- | ----------- | ------- | --------- | ----------------- | -------------------------------------------------------------- |
| intel  | Core         | Core 2      | LGA775  | DDR2-DDR3   | 8GB     | 2006-2007 |                   | Énorme gain de performance par rapport à Netburst              |
| intel  | Penryn       | Core 2      | LGA775  | DDR2-DDR3   | 8GB     | 2007-2008 |                   | Meilleure efficacité énergétique                               |
| intel  | Nehalem      | 1re gén.    | LGA1156 | DDR3        | 16GB    | 2008-2009 |                   | SMT, contrôleur mémoire sur le CPU et quad-core monolithique   |
| intel  | Westmere     | 1re gén.    | LGA1156 | DDR3        | 16GB    | 2010-2011 |                   | Meilleure efficacité énergétique                               |
| intel  | Sandy Bridge | 2e gén.     | LGA1155 | DDR3        | 32GB    | 2011-2012 | M72 tiny          | Ajout du support AVX, bon iGPU et forte hausse des perfs       |
| intel  | Ivy Bridge   | 3e gén.     | LGA1155 | DDR3        | 32GB    | 2012-2013 | M72 tiny          | Meilleure efficacité énergétique                               |
| intel  | Haswell      | 4e gén.     | LGA1150 | DDR3        | 32GB    | 2013-2014 | M73 tiny          | Support d'AVX2 et FMA3, meilleures perfs                       |
| intel  | Broadwell    | 5e gén.     | LGA1150 | DDR3        | 32GB    | 2014-2015 |                   | Meilleure efficacité énergétique                               |
| intel  | Skylake      | 6e gén.     | LGA1151 | DDR3-DDR4   | 64GB    | 2015-2016 | M700, M710q       | Enc./déc. matériel HEVC/VP9 8 bits, iGPU Vulkan et support NVMe |
| intel  | Kaby Lake    | 7e gén.     | LGA1151 | DDR4        | 64GB    | 2016-2017 | M710q             | Support de l'enc./déc. matériel HEVC/VP9 10 bits               |
| intel  | Coffee Lake  | 8-9e gén.   | LGA1151 | DDR4        | 64GB    | 2017-2019 | M720q             | Hausse du nombre de cœurs et suppression du SMT sur la 9e gén. |
| intel  | Comet Lake   | 10e gén.    | LGA1200 | DDR4        | 128GB   | 2020-2021 | M70q gen 1        | Réintroduction du SMT sur la plupart des CPU                   |
| intel  | Rocket Lake  | 11e gén.    | LGA1200 | DDR4        | 128GB   | 2021-2022 | M70q gen 2        | Ajout du support AVX-512 et meilleures perfs                   |
| intel  | Alder Lake   | 12e gén.    | LGA1700 | DDR4-DDR5   | 256GB   | 2021-2022 | M70q gen 3        | Suppression d'AVX-512, Pcore et Ecore, déc. matériel AV1 et IPC en hausse |
| intel  | Raptor Lake  | 13-14e gén. | LGA1700 | DDR5        | 256GB   | 2022-2023 | M70q gen 4, 5     | Plus d'Ecores et de cache                                      |
| intel  | Arrow Lake   | ?           | LGA1700 | DDR5        | 256GB   | 2024-2025 | M70q gen 6        | Suppression du SMT, gros gain de perf par thread, encodage AV1, Ray Tracing |
| intel  | Nova Lake    | ?           | LGA1851 | DDR5        | ?       | 2026 ?    |                   | (Ré)introduction du support AVX10.2/AVX512                     |

#### Générations de CPU AMD

| Marque | Arch. CPU | Gén. CPU | Socket | Type de RAM | RAM max | Année     | Exemple de PC SFF | Remarques                                                          |
| ------ | --------- | -------- | ------ | ----------- | ------- | --------- | ----------------- | ----------------------------------------------------------------- |
| AMD    | Excavator | 4e gén.  | AM4    | DDR4        | 32GB    | 2015-2016 |                   |                                                                   |
| AMD    | Zen       | 1re gén. | AM4    | DDR4        | 64GB    | 2017-2018 | M715Q             | Énorme gain de performance, au niveau des CPU Intel Haswell/Broadwell |
| AMD    | Zen+      | 2e gén.  | AM4    | DDR4        | 64GB    | 2018-2019 |                   |                                                                   |
| AMD    | Zen 2     | 3e gén.  | AM4    | DDR4        | 128GB   | 2019-2020 | M70q gen 1/2      | Au niveau des CPU Intel Skylake et corrige la plupart des problèmes de Zen |
| AMD    | Zen 3     | 4e gén.  | AM4    | DDR4        | 128GB   | 2020-2021 | M70q gen 2        | Amélioration de l'IPC et de l'efficacité énergétique              |
| AMD    | Zen 4     | 5e gén.  | AM5    | DDR5        | 128GB   | 2021-2022 |                   | Ajout du support AVX-512, meilleur IPC et iGPU RDNA 3             |
| AMD    | Zen 5     | 6e gén.  | AM5    | DDR5        | 192GB   | 2022-2023 | M70q gen 5        | Légère amélioration de l'IPC et des perfs AVX-512                 |

Je recommande d'aller vers les CPU **Intel Alder Lake**, **AMD Zen 3** ou plus récents, ils offrent de belles performances et prennent en charge les fonctionnalités modernes comme le NVMe, le Vulkan sur iGPU, l'encodage/décodage matériel HEVC 10 bits, l'AVX2, etc. 

Cependant, si vous avez un budget serré, les **Intel Coffee Lake** et **AMD Zen 2** restent une bonne option grâce au faible prix et à leurs performances correctes, les CPU plus anciens comme les **Intel Haswell** et **AMD Excavator** ne valent souvent pas le coup en raison de leurs faibles performances, de l'absence de fonctionnalités modernes (NVMe, HEVC, Vulkan, etc.) et de mises à jour de microcode (correctifs de sécurité et de bugs pour le CPU).

### GPU (Graphics Processing Unit)

La plupart des PC SFF ne disposent que d'un GPU intégré, ceux-ci suffisent pour les tâches graphiques légères et sont très économes en énergie, certains PC SFF peuvent accueillir un GPU dédié (comme les M720Q/M920Q),ces cartes sont low-profile et utilisent des lignes PCIe x4/x8, ce qui peut être utile pour du jeu léger, du réseau, etc. **Assurez-vous que le PSU et la carte mère peuvent supporter la consommation électrique de la carte PCIe.**

Je recommande les iGPU Intel à partir de **Skylake ou plus récents** (Intel HD série 500 et plus récents) ou les iGPU AMD à partir de **Zen 2 ou plus récents** (Vega et plus récents), ces GPU prennent en charge les API graphiques modernes comme OpenGL 4.6 et Vulkan 1.4*, et offrent une accélération matérielle pour les codecs vidéo courants comme AVC/H.264, HEVC/H.265 et VP9.

Le décodage matériel AV1 est disponible sur Intel Alder Lake ou plus récent, et sur les iGPU basés sur AMD RDNA2/Zen 3+ ou plus récents, pour l'encodage, il faut des GPU Intel Arc, Arrow Lake ou des GPU basés sur AMD RDNA3/Zen 4.

*: Vulkan permet aujourd'hui de décoder et encoder des vidéos à la place des API traditionnelles comme VA-API ou VDPAU.

### RAM (Random Access Memory)

Les PC SFF disposent généralement de **deux slots de RAM**, prenant en charge la RAM DDR3, DDR4 ou DDR5 **selon le CPU et la carte mère**, la capacité maximale va habituellement de 16GB à 256GB, je recommande d'utiliser **deux barrettes de RAM identiques** pour activer le dual-channel (double la bande passante). 

**Vous pouvez utiliser de la RAM avec une fréquence plus élevée que celle officiellement prise en charge par le CPU/Carte mère, la RAM se cadencera automatiquement à la fréquence maximale supportée par le contrôleur mémoire et la carte mère.**

La plupart des PC SFF prennent en charge la **SO-DIMM** (RAM au format PC portable), plus petite que la RAM DIMM standard, mais avec des performances similaires.

Voici quelques recommandations générales (en 2026) :

- **4GB** : serveur Linux minimaliste, applications légères (hébergement de petit site web, routeur, NAS)
- **8GB** : applications légères à moyennes (navigation web, bureautique, petits serveurs)
- **16GB** : recommandé pour la plupart des usages (serveur de jeu basique, serveur de build CI, développement léger)
- **32GB+** : optimal pour le multitâche (jeux AAA, montage vidéo/photo, rendu)
- **64GB+** : multitâche intensif (virtualisation, machine learning, calcul scientifique, CAO)

### Stockage

Les PC SFF disposent de **quatre principales options de stockage** (selon le modèle) :

- **SSD M.2 NVMe** : très rapide et présent dans la plupart des PC SFF depuis 2015, le meilleur choix.
- **SSD M.2 SATA** : utilise le même connecteur que le NVMe mais fonctionne avec le protocole SATA (ex. ThinkCentre M700).
- **SSD 2.5" SATA** : plus lent que le M.2 NVMe mais une bonne alternative si le M.2 n'est pas disponible.
- **HDD 2.5" SATA** : très lent et généralement déconseillé, mais peut être remplacé par un SSD.
- **eMMC embarquée** : stockage soudé sur la carte mère, **à éviter** : lent, limité et **non remplaçable**.

Je recommande d'utiliser des **SSD M.2 NVMe**, faites attention à la taille (2242, 2260, 2280), au type de connecteur (B, M, B+M) et au fait que le SSD soit simple ou double-face.

Vous pouvez utiliser des SSD **PCIe 4.0 x4** sur des slots **PCIe 3.0 x2** ou **x4** et inversement, **le SSD s'ajustera automatiquement à la vitesse maximale supportée par les deux éléments.**

### Ports

Tous les PC SFF ont un nombre limité de ports, assurez-vous que le PC SFF choisi dispose de suffisamment de ports pour vos besoins, certains modèles permettent d'ajouter des ports supplémentaires (la plupart des ThinkCentre Tiny de Lenovo).

Les ports courants incluent :

- **USB type A** : pour les périphériques, le stockage, la souris, le clavier, etc.
- **USB type C** : comme l'USB type A, parfois avec sortie vidéo et/ou support Thunderbolt.
- **HDMI/DisplayPort/VGA** : pour les écrans.
- **Ethernet** : pour le réseau.
- **Prises audio** : pour les casques, micros et haut-parleurs.

### PSU (Power Supply Unit)

La plupart des PC SFF utilisent une **alimentation externe**, souvent avec un connecteur propriétaire.

Voici quelques repères généraux :

- **45W** : CPU 15W
- **65W** : CPU 35W
- **90W** : CPU 65W ou CPU 35W + lecteur DVD/extension
- **135W** : CPU 65W + GPU 45W ou CPU 100W

Vous pouvez obtenir de **petits gains de performance** en utilisant un PSU surdimensionné, surtout depuis les CPU Intel **Comet Lake** et plus récents.

### Carte mère

Comme pour le PSU, la plupart des PC SFF ont une **carte mère propriétaire**, il est parfois possible de la remplacer par un autre modèle de la même marque (ex. : une carte mère de M920Q dans un M720Q), mais dans la plupart des cas, il vaut mieux conserver le modèle de carte mère d'origine.

### Système d'exploitation

Tous les PC SFF basés sur x86 sont compatibles avec la plupart des systèmes d'exploitation (Linux, Windows, FreeBSD, même macOS x86, etc.), je recommande fortement d'utiliser **Linux** ou **FreeBSD** en raison de leur faible consommation de ressources, de leurs meilleures performances, de leur sécurité et de leur compatibilité avec le matériel plus ancien.

Voici quelques distributions Linux que je recommande pour les PC SFF:

Distributions Linux standard :

- **Debian** : stable, bien supportée, vaste dépôt logiciel, cycle de mise à jour d'environ 2 ans.
- **Ubuntu** : conviviale, grande communauté, basée sur Debian avec le bureau GNOME.
- **Arch Linux** : rolling release et logiciels de pointe, très personnalisable mais courbe d'apprentissage élevée.
- **NixOS** : configuration entièrement déclarative et reproductible, système de gestion de paquets unique, apprentissage difficile mais très puissant.

Distributions Linux légères :

- **Lubuntu** : Ubuntu avec l'interface LXQt.
- **Xubuntu** : Ubuntu avec l'interface XFCE.
- **SliTaz** : extrêmement léger, peut tourner sur du matériel très ancien mais avec des noyaux et logiciels anciens.

Distributions Linux orientées multimédia :

- **OSMC** : distribution légère de type media center basée sur Debian.

## PC SFF Lenovo ThinkCentre

Dans cette section, nous allons voir les différents modèles de PC SFF Lenovo ThinkCentre.

| Modèle     | CPU                      | Chipset         | RAM SODIMM²          | PCIe      | Ports SSD/HDD         | PSREF                                                                                                               |
| ---------- | ------------------------ | --------------- | -------------------- | --------- | --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| M72 tiny   | Sandy Bridge/Ivy Bridge  | Intel H61       | 2x 8GB 1600MHz DDR3  | -         | 1x SATA               | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/M72e.pdf)                                              |
| M92 tiny   | Sandy Bridge/Ivy Bridge  | Intel Q77       | 2x 8GB 1600MHz DDR3  | -         | 1x SATA               | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/M92&M92p.pdf)                                          |
| M73 tiny   | Haswell                  | Intel H81       | 2x 8GB 1600MHz DDR3  | -         | 1x SATA               | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M73_Tiny/ThinkCentre_M73_Tiny_Spec.pdf)      |
| M83 tiny   | Haswell                  | Intel Q85       | 2x 8GB 1600MHz DDR3  | -         | 1x SATA               | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M83_Tiny/ThinkCentre_M83_Tiny_Spec.pdf)      |
| M700q      | Skylake                  | Intel B150      | 2x 16GB 2133MHz DDR4 | -         | 1x SATA & 1x (SATA)   | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M700_Tiny/ThinkCentre_M700_Tiny_Spec.pdf)    |
| M900q      | Skylake                  | Intel Q170      | 2x 16GB 2133MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M900_Tiny/ThinkCentre_M900_Tiny_Spec.pdf)    |
| M710q      | Skylake/Kaby Lake        | Intel B250      | 2x 32GB 2400MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M710_Tiny/ThinkCentre_M710_Tiny_Spec.pdf)    |
| M910q      | Skylake/Kaby Lake        | Intel Q270      | 2x 32GB 2400MHz DDR4 | -         | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M910_Tiny/ThinkCentre_M910_Tiny_Spec.pdf)    |
| M720q      | Coffee Lake              | Intel B360      | 2x 32GB 2666MHz DDR4 | x8 Gen 3¹ | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M720_Tiny/ThinkCentre_M720_Tiny_Spec.pdf)    |
| M920q      | Coffee Lake              | Intel Q370      | 2x 32GB 2666MHz DDR4 | x8 Gen 3¹ | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M920_Tiny/ThinkCentre_M920_Tiny_Spec.pdf)    |
| M920x      | Coffee Lake              | Intel Q370      | 2x 32GB 2666MHz DDR4 | x8 Gen 3¹ | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M920x_Tiny/ThinkCentre_M920x_Tiny_Spec.pdf)  |
| P330       | Coffee Lake              | Intel Q370      | 2x 32GB 2666MHz DDR4 | x8 Gen 3¹ | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkStation/ThinkStation_P330_Tiny/ThinkStation_P330_Tiny_Spec.pdf) |
| M75q       | AMD Zen 2                | AMD Pro 500     | 2x 32GB 2933MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M75q_Tiny/ThinkCentre_M75q_Tiny_Spec.PDF)    |
| M75q Gen 2 | AMD Zen 3                | AMD Pro 500     | 2x 32GB 3200MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M75q_Gen_2/ThinkCentre_M75q_Gen_2_Spec.pdf)  |
| M70q       | Comet Lake               | Intel H470      | 2x 32GB 2933MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q/ThinkCentre_M70q_Spec.pdf)              |
| M80q       | Comet Lake               | Intel Q470      | 2x 32GB 2933MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M80q/ThinkCentre_M80q_Spec.pdf)              |
| M90q       | Comet Lake               | Intel Q470      | 2x 32GB 2933MHz DDR4 | x8 Gen 3  | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M90q/ThinkCentre_M90q_Spec.pdf)              |
| P340       | Comet Lake               | Intel Q470      | 2x 32GB 2933MHz DDR4 | x8 Gen 3  | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkStation/ThinkStation_P340_Tiny/ThinkStation_P340_Tiny_Spec.pdf) |
| M70q Gen 2 | Rocket Lake/Comet Lake   | Intel B560      | 2x 32GB 3200MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q_Gen_2/ThinkCentre_M70q_Gen_2_Spec.pdf)  |
| M90q Gen 2 | Rocket Lake/Comet Lake   | Intel Q570      | 2x 32GB 3200MHz DDR4 | x8 Gen 3  | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M90q_Gen_2/ThinkCentre_M90q_Gen_2_Spec.pdf)  |
| P350       | Rocket Lake              | Intel Q570      | 2x 32GB 3200MHz DDR4 | x8 Gen 3  | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkStation/ThinkStation_P350_Tiny/ThinkStation_P350_Tiny_Spec.pdf) |
| M80q Gen 3 | Alder Lake               | Intel Q670      | 2x 32GB 4800MHz DDR5 | -         | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M80q_Gen_3/ThinkCentre_M80q_Gen_3_Spec.pdf)  |
| M90q Gen 3 | Alder Lake               | Intel Q670      | 2x 32GB 4800MHz DDR5 | x8 Gen 4  | 1x SATA & 2x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M90q_Gen_3/ThinkCentre_M90q_Gen_3_Spec.pdf)  |
| P360       | Alder Lake               | Intel Q670      | 2x 32GB 4800MHz DDR5 | x8 Gen 4  | 2x M.2 NVMe           | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkStation/ThinkStation_P360_Tiny/ThinkStation_P360_Tiny_Spec.pdf) |
| M70q Gen 3 | Alder Lake               | Intel Q670      | 2x 32GB 3200MHz DDR4 | -         | 1x SATA & 1x M.2 NVMe | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q_Gen_3/ThinkCentre_M70q_Gen_3_Spec.pdf)  |
| M75q Gen 5 | AMD Zen 4                | AMD Pro 600     | 2x 32GB 5200MHz DDR5 | -         | 2x M.2 NVMe           | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M75q_Gen_5/ThinkCentre_M75q_Gen_5_Spec.pdf)  |
| M70q Gen 4 | Raptor Lake              | Intel Q670      | 2x 32GB 5600MHz DDR5 | -         | 2x M.2 NVMe           | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q_Gen_4/ThinkCentre_M70q_Gen_4_Spec.pdf)  |
| M70q Gen 5 | Raptor Lake              | Intel Q670      | 2x 32GB 5600MHz DDR5 | -         | 2x M.2 NVMe           | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q_Gen_5/ThinkCentre_M70q_Gen_5_Spec.pdf)  |
| M70q Gen 6 | Arrow Lake               | Intel B860/Q870 | 2x 32GB 5600MHz DDR5 | -         | 2x M.2 NVMe           | [PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkCentre/ThinkCentre_M70q_Gen_6/ThinkCentre_M70q_Gen_6_Spec.pdf)  |

**¹** : vous avez besoin d'une carte riser propriétaire pour utiliser le slot PCIe.

**²** : la RAM maximale supportée est déterminée par le CPU (contrôleur mémoire) et le BIOS, certaines configurations peuvent prendre en charge davantage de RAM que les spécifications officielles.

### Outils

Simulateur de BIOS/UEFI Lenovo : [Simulateur](https://download.lenovo.com/bsco/index.html#/)

### M710q et M910q

#### Ports

{{ img(src="/images/articles/SSF-PC/lenovo-thinkcentre-m710q-front.webp" class="" alt="Face avant du M710q" caption="Face avant du M710q" link="") }}

Sur la face avant :

- 2x USB 3.1 Gen 1
- 1x prise casque audio
- 1x prise micro audio

{{ img(src="/images/articles/SSF-PC/lenovo-thinkcentre-m710q-back.webp" class="" alt="Face arrière du M710q" caption="Face arrière du M710q" link="") }}

Sur la face arrière :

- 4x USB 3.1 Gen 1
- 1x HDMI 1.4
- 1x DisplayPort 1.2a
- 1x Ethernet RJ45
- 1x connecteur d'alimentation propriétaire Lenovo
- 2x port propriétaire pour accessoires (VGA, HDMI, DP, USB-C, etc.)

Le M710q/M910q ne prend pas en charge le HDR via HDMI (1.4) ou DisplayPort (1.2a), mais la profondeur de couleur 10 bits est supportée.

#### CPU

Le M710q/M910q prend en charge tous les CPU Intel 35 W de **6e** et **7e** génération (modèles avec le suffixe **T**), je recommande la 7e génération pour le support de l'encodage/décodage matériel HEVC 10 bits.

#### RAM

Le M710q/M910q dispose de **deux slots SODIMM DDR4** avec une capacité maximale de **32GB** (2x16GB), la fréquence maximale est de **2133MHz**, ou **2400MHz** sur la **7e** génération.

#### BIOS

Vous **devriez** mettre à jour votre BIOS pour améliorer la compatibilité avec le matériel récent, les anciennes versions du BIOS posent problème avec certains SSD NVMe : [reddit](https://www.reddit.com/r/Lenovo/comments/1jzxnp4/m710q_tiny_what_nvme_ssd_works/?show=original)

#### Dépannage

### M720q, M920q et M920x

#### Ports

{{ img(src="/images/articles/SSF-PC/lenovo-thinkcentre-m720q-front.webp" class="" alt="Face avant du M720q" caption="Face avant du M720q" link="") }}

Sur la face avant :

- Le bouton d'alimentation
- 1x prise micro audio
- 1x prise casque audio
- 1x USB-C 3.1 Gen 1
- 1x USB 3.1 Gen 1

{{ img(src="/images/articles/SSF-PC/lenovo-thinkcentre-m720q-back.webp" class="" alt="Face arrière du M720q" caption="Face arrière du M720q" link="") }}

Sur la face arrière :

- 1x connecteur d'alimentation propriétaire Lenovo
- 1x DisplayPort 1.2a
- 2x USB 3.1 Gen 1
- 1x HDMI 1.4
- 2x USB 3.1 Gen 2
- 1x Ethernet RJ45
- 2x port pour accessoires propriétaires (VGA, HDMI, DP, USB-C, etc.)

Le M720q/M920q ne prend pas en charge le HDR via HDMI (1.4) ou DisplayPort (1.2a), mais la profondeur de couleur 10 bits est supportée.

#### CPU

Le M720q/M920q prend en charge tous les CPU Intel 35 W de **8e** et **9e** génération (modèles avec le suffixe **T**), l'**i7-9900T** est le CPU le plus puissant disponible pour ce modèle, mais il est très cher et difficile à trouver, les i3-8100T, i3-9100T, i5-8500T, i5-8600T, i5-9500T, i5-9600T, i7-8700T et i7-9700T sont bien plus courants, abordables et offrent malgré tout de bonnes performances.

Évitez les Celeron et Pentium, ils sont assez lents (dépourvus d'AVX2, FMA3, etc.), **N'utilisez pas de CPU dont le TDP dépasse 35 W (65 W sur le M920x)**, cela peut provoquer une surchauffe et potentiellement endommager votre carte mère (comme les VRM) ou le PSU.

#### RAM

Le M720q/M920q/M920x dispose de **deux slots SODIMM DDR4** avec une capacité maximale de **64GB** (2x32GB), la fréquence maximale est de **2400MHz**, ou **2666MHz** sur les CPU i5/i7.

#### Stockage

Vous avez **deux** options de stockage :

- **M.2 NVMe PCIe 3.0** : un seul slot, en PCIe x4 Gen 3.
- **2.5" SATA** : plus lent, mais une bonne alternative si vous avez besoin de plus de stockage ou si vous n'avez pas de SSD M.2 NVMe.

Il manque le NVMe sur le **second slot M.2** des M720q/M920q ; vous pouvez souder les composants manquants pour obtenir un M.2 (SATA) fonctionnel : [https://github.com/badger707/m920q-dual-NVME](https://github.com/badger707/m920q-dual-NVME)

#### GPU

Tous les CPU compatibles disposent d'un GPU intégré, si cela ne suffit pas, vous pouvez ajouter un GPU **low-profile** via une **carte riser PCIe propriétaire** ; vous êtes limité au PCIe 3.0 x8 et à un TDP de 45 W (il faut aussi un PSU de 135 W).

#### PSU

Le PSU propriétaire utilisé pour le M720q existe en **65W**, **90W** et **135W** ; **90W** est le minimum lorsque vous utilisez des cartes d'extension ou un CPU puissant (i7 ou i9).

#### Extensions et accessoires

Le M720q prend en charge plusieurs options d'extension :

| Type                     | Modèle     | Description                       |
| ------------------------ | ---------- | --------------------------------- |
| Carte port VGA           | 01AJ935    | Ajoute 1 sortie port VGA          |
| Carte port VGA           | 5C50W00881 | Ajoute 1 sortie port VGA          |
| Carte port DisplayPort   | 01AJ937    | Ajoute 1 sortie port DisplayPort  |
| Carte port HDMI          | 01AJ938    | Ajoute 1 sortie port HDMI         |
| Carte port USB-C         | 01AJ939    | Ajoute 1 sortie port USB-C        |
| Riser PCIe x8            | 01AJ940    | Ajoute 1 slot PCIe x8             |
| Carte port COM RS232     | 04X2733    | Ajoute 1 sortie port COM RS232    |
| Support VESA             | 4XF0N03161 | Support VESA + vis                |
| Support VESA             | SM10U47670 | Support VESA + vis                |
| Support VESA             | 01EF310    | Support VESA + vis                |
| Support VESA             | 01EF645    | Support VESA + vis                |
| Support VESA             | 5M10U49625 | Support VESA + vis                |
| Hub USB                  | 01EF647    | Hub USB avec RS232                |
| Antenne Wifi             | 00XJ126    | Antenne Wifi interne              |
| Radiateur avec ventilo   | 01MN633    | Radiateur avec ventilateur        |
| Radiateur avec ventilo   | 01MN632    | Radiateur avec ventilateur        |

#### BIOS

Pour mettre à jour le BIOS, vous **devez** d'abord mettre à jour l'**Intel Management Engine**, puis mettre à jour le BIOS, sinon vous risquez un boot loop avec les anciennes versions du BIOS.

#### Dépannage

## Sources

- [Project TinyMiniMicro](https://forums.servethehome.com/index.php?threads/lenovo-thinkcentre-thinkstation-tiny-project-tinyminimicro-reference-thread.34925/)
- [Tiny/Mini/Micro PC experiences](https://forums.servethehome.com/index.php?threads/tiny-mini-micro-pc-experiences.30230/)
- [Wikipedia](https://en.wikipedia.org/wiki/Small_form_factor)
- [cpu-world](https://www.cpu-world.com/)
