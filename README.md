[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/radituye/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/radituye/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The World in One Image — Tuesday, 17 November 2026

A front page that sums up the world news of Tuesday 17 November 2026, for
the make.fun bounty: https://make.fun/bounty/news-image-20261117

![The World in One Image — 17 November 2026](image.png)

## What the image shows

- **Lead — Kerch Bridge hit:** Ukraine struck the bridge linking Russia to
  occupied Crimea and a road span collapsed; Russia answered with missile
  strikes on Kyiv's bridges over the Dnipro.
- **Trump in Manila:** the US president arrived in the Philippines for his
  Asia trip, ahead of trilateral talks with Xi Jinping and Vladimir Putin
  on nuclear issues, Ukraine and trade.
- **Tankers hit in Hormuz:** two tankers struck mines in the Strait of
  Hormuz as a third US aircraft carrier reached the Middle East.
- **Vulcan rocket fails:** a launch anomaly destroyed 40 Amazon Leo
  internet satellites.
- **JPMorgan outage:** the bank blamed a software bug, not a cyberattack,
  for Monday's banking disruption.
- **Also:** the Pentagon failed its financial audit for a ninth year;
  Nvidia reported its first earnings since Jensen Huang's exit; Estonia
  announced it will shut its Russia border crossings on 1 December; Japan
  scrambled jets after Russian aircraft entered its airspace; five EU
  states outlined a joint migrant return hub in Rwanda.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`image.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
outside the grader). The image is a 1024×1024 PNG under 1 MiB, built from
a generated illustration of the collapsed bridge plus crisp typeset
headlines, so two runs write byte-identical output and it needs no
network at run time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```
