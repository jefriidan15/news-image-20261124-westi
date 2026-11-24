# The World in One Page — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/competitions/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jefriidan15/news-image-20261124-westi/rank.svg)](https://make.fun/competitions/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jefriidan15/news-image-20261124-westi/reward.svg)](https://make.fun/competitions/news-image-20261124)

A single newspaper-style front page that sums up the world's news of
**Tuesday 24 November 2026** in one image — the date is printed on the
page itself, so the image stands alone with no news feed attached.

## What's on the page

- **South Korea island alert** — an evacuation warning briefly issued for
  Ulleung island on Tuesday morning (07:52 KST, lifted after 3 minutes)
  after an aircraft entered its airspace.
- **Finland summons the Russian envoy** — Helsinki summons Moscow's
  ambassador over the suspected Russian helicopter incursion off Loviisa
  (21 November, 4.1 km inside Finnish airspace).
- **World Chess Championship, Game 1** — Gukesh defends his title against
  Sindarov in Geneva, 15:00 CET, the youngest title match ever, $2.5m prize.
- **Also today:** the Beaver Supermoon peaks (9:53 a.m. EST / 14:53 UTC),
  Dell & HP report earnings after the US close, and Guru Nanak's 557th
  birth-anniversary celebrations enter their second day.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory (`MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output`), as `/output/entry.png`.

```sh
python3 main.py
```

The front page itself is rendered locally with Pillow by
`work/gen_image.py` and committed as `entry.png` (1024×1024, under 1 MiB),
so the entry program needs no network and no extra packages at run time.

## Referral

Play code: `s7vdxe79`
