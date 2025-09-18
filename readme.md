# Grackle-CSI in CoCo2025

Grackle-CSI solves the largest number of problems in the term rewrite system (TRS) category of [CoCo2025](https://project-coco.uibk.ac.at/2025/).  

CoCo is the annual international competition on confluence analysis, a core topic in term rewrite systems—with deep ties to computability theory going back to Church & Turing.
TRS is the most classic and important category in CoCo.

Grackle-CSI uses machine learning techniques to automatically invent strategies for the confluence tool CSI.

This is the first time AI techniques have been combined with term rewrite tools, marking a milestone in applying AI to formal reasoning.
Just like AI has transformed Go playing and protein discovery, it now shows strong potential in automated reasoning and formal mathematics.

Confluence analysis is closely related to program equivalence, termination, and automated proof systems. AI can open new pathways for advances across these areas.
We see this as a step toward the future of AI + formal methods: combining symbolic rigor with data-driven learning to tackle problems beyond human reach.


## Results

**Results of CoCo competition**.
It contains 100 term rewrite systems (TRSs) randomly chosen from the ARI-COPS database.
| Solver | YES | NO | Total | Rank |
| ---- |-----|----|-------|------|
| Grackle-CSI | 50  | 34 | 84    | **1st** |
| CSI    | 51 | 33  | 84 | **1st** |
| ACP    | 48 | 26| 74   | **3rd** |

**Results of CoCo's full run**.
The timeout is one minute.

| Solver | YES | NO | Total | Rank |
| ---- |-----|----| ------|------|
| Grackle-CSI | 277  | 206 | 483     | **1st** |
| CSI    | 272 | 205  | 477 | **2nd** |
| ACP    | 257 | 164 | 421  | **3rd** |

**Results of CoCo's full run 10min**.
| Solver | YES | NO | Total | Rank |
| ---- |-----|----| ------|------|
| Grackle-CSI | 277  | 206 | 483     | **1st** |
| CSI    | 274 | 205  | 479 | **2nd** |
| ACP    | 258 | 168 | 426  | **3rd** |


During the competition, Grackle-CSI ranked first only in the non-confluence analysis (NO category), since it occasionally produced warnings (as shown in the screenshot below). However, in CoCo’s statistics, an answer is considered valid only when the first line of output is either YES or NO.

<div align = "center">
<img src = "yes.png" width = "400" height = "330">
</div>


## Run

The statistics in the repository do not ignore proofs that have warnings. The logs of problem solving were downloaded from [CoCo25's full run statistics](https://ari-cops.uibk.ac.at/CoCo/2025/full-run/TRS/), [CoCo25's competition statistics](https://ari-cops.uibk.ac.at/CoCo/2025/full-run/TRS/) and [CoCo25's 10 mintue-full run statistics](https://ari-cops.uibk.ac.at/CoCo/2025/full-run10m/TRS/).

To obtain the statistics, run

`python coco2025.py --results_dir coco2025-competition/  --stats_file  coco2025_competition_stats.json`

`python coco2025.py --results_dir coco2025-full/  --stats_file  coco2025_full_stats.json`

`python coco2025.py --results_dir coco2025-full-10min/  --stats_file  coco2025_full_10min_stats.json`

## Reference



[Automated Strategy Invention for Confluence of Term Rewrite Systems](https://arxiv.org/abs/2505.07270). Liao Zhang, Fabian Mitterwallner, Jan Jakubuv, Cezary Kaliszyk. IJCAI 2025.

```
@article{zhang2024automated,
  title={Automated Strategy Invention for Confluence of Term Rewrite Systems},
  author={Zhang, Liao and Mitterwallner, Fabian and Jakubuv, Jan and Kaliszyk, Cezary},
  journal={IJCAI},
  year={2025}
}
```