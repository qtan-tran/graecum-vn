# Graecum VN – Ancient Greek

**A completely free self-study hub for Ancient Greek**, taking learners from zero to reading Plato, Xenophon, the Greek New Testament (Koine) and other intermediate–advanced texts.

> All content: **CC BY-SA 4.0** · Code: **MIT** · Compiled by **Trần Quốc Tân** · No ads, no paywall, no data collection.

**Start right away – the portal links straight into every lesson:** **https://qtan-tran.github.io/graecum-vn/**

**English edition** of the repository. Original (Tiếng Việt): [README.md](README.md) · [English portal](https://qtan-tran.github.io/graecum-vn/en/)

## Why this project?

- High-quality free material for Ancient Greek exists online (Perseus, Scaife, Logeion, public-domain grammars), but it is **scattered** and comes **without a path**: no unified route from absolute beginner to reading real texts.
- This project is a **path + lessons + readings + tools** that ties everything together, so a self-learner has **a single place to start and keep going**.

## The 48-lesson path (2 levels)

| Level | Lessons | Exit goal |
| --- | --- | --- |
| **Graecum I** (equivalent to the Graecum certificate level) | 1–24 | Complete morphology (declensions, verbs in all tenses/moods) + foundational syntax; read simple Attic prose (adapted Xenophon) with a dictionary. |
| **Graecum II** | 25–48 | Advanced syntax (participle, optative, indirect speech, articular infinitive…) and read intermediate–advanced original texts: Plato, Xenophon, Euripides, NT, Homer, Herodot. |

In total **48 lessons + 10 review lessons (Wiederholung)**: after every five lessons there is a review lesson (Review #1 after Lesson 5, #2 after Lesson 10 … #10 after Lesson 48), each with a grammar summary, morphology overview tables, an Anki vocabulary deck for the five-lesson block, and a review strategy.

**Graecum I (Lessons 1–24)** in five blocks:

- **Lessons 1–5 – foundations:** alphabet & accents, word classes, the article, o-declension nouns, present active verbs, first infinitives, middle/passive & deponents, pronouns; dative & accusative. Readings: Homer, Mimnermos, Plato, Epicurus, Marcus Aurelius.
- **Lessons 6–10 – the full nominal system:** 3rd declension (consonant & vowel stems, neuters), numerals 1–999, 3/2-ending adjectives & adverbs, the full imperative system, prohibitions. Readings: Homer, Dio, Longos, Plutarch, Plato, Xenophon.
- **Lessons 11–15 – the past system:** imperfect & augment, future, aorist (sigmatic & thematic), passive, perfect middle/passive; relative pronouns & clauses. Readings: Herodotus, Diodorus, Xenophon, Plutarch, Aristides, Plato, Apollodorus.
- **Lessons 16–20 – moods & clause syntax:** subjunctive & purpose clauses, optative & indirect speech, extended accusative-with-infinitive & indirect questions, participles I–II (attributive, circumstantial, AccP, genitive absolute). Readings: Athenaeus, Parthenius, Plato, Aesop, Arrian, Longos, Dio Chrysostomos, Isocrates.
- **Lessons 21–24 – finishing Graecum I:** conditionals, temporal/causal clauses, athematic verbs (δίδωμι, τίθημι, ἵστημι, φημί), a capstone reading of continuous Xenophon prose. Readings: Euripides, Theophrastus, Xenophon, Lucian, Aelian.

**Graecum II (Lessons 25–48)** in five blocks:

- **Lessons 25–29:** systematic indirect speech & sequence of tenses, result clauses, articular infinitive, fear/effort clauses. Readings: Lysias, Aristophanes, Apollodorus, Plato, Aesop, Euripides.
- **Lessons 30–34:** periodic style, counterfactual conditionals, the ἄν system, then **Koine & Biblical Greek** (Mark, Matthew, Pauline letters) contrasted with Attic. Readings: Plato, Plutarch, Polyainos, NT.
- **Lessons 35–39:** narrative historiography, deliberative prose, **the epic dialect & hexameter (Homer)**, late Greek, Socratic literature. Readings: Xenophon, Philostratos, Homer, Plato.
- **Lessons 40–44:** distinctive styles: Lucianic satire, **epigraphy (reading inscriptions)**, myth in philosophy, ekphrasis & travel writing, fable. Readings: Lucian, the Epidaurus inscription, Plato, Pausanias, Aesop.
- **Lessons 45–48:** argument analysis, moral narrative, dialogue, and a capstone of **reading unadapted originals**; a full-system review. Readings: Plato, Xenophon.

Every lesson has 1–2 **readings** from **public-domain** originals (with grammatical analysis), ~18 vocabulary items with **Latinized transliteration**, a confusables table, and exercises with hidden answers (revealed when printing).

Details: [docs/CURRICULUM.md](docs/CURRICULUM.md) · Published lessons: [portal](https://qtan-tran.github.io/graecum-vn/)

## Companion toolkit – Ancient Greek Toolkit

The companion tools repository: **[ancient-greek-toolkit](https://github.com/qtan-tran/ancient-greek-toolkit)** – open it directly at **https://qtan-tran.github.io/ancient-greek-toolkit/** (Vietnamese edition; [English edition](https://qtan-tran.github.io/ancient-greek-toolkit/en/)): lexica & morphology lookup (Logeion, Wiktionary), primary-text libraries (Perseus, Scaife, Theoi), typing Greek & fonts, practice & Anki, reference grammar (public-domain Smyth), resource comparisons, and **YouTube channels** for Ancient Greek.

## Repository structure

```
├── index.html              # Portal (GitHub Pages) – https://qtan-tran.github.io/graecum-vn/
├── en/                     # English edition: portal + lesson translations
├── lessons/                # 48 lessons, each one self-contained HTML file (Vietnamese)
├── readings/               # Public domain texts + simplified versions with analysis
├── vocab/                  # Vocabulary per lesson, with Latinized transliteration; Anki decks
├── docs/                   # Architecture, style conventions, copyright, roadmap
└── toolkit.md              # Points to the separate ancient-greek-toolkit repo (bilingual VI/EN hub)
```

## How to use the lessons

1. Read them directly on the web: **[portal](https://qtan-tran.github.io/graecum-vn/)** or **download** the single HTML file.
2. Study offline: open the HTML file in any browser – no internet needed, no third-party dependencies.
3. To print: open the file → **Ctrl+P → Save as PDF** – exercise answers appear automatically when printing.
4. Drill vocabulary with spaced repetition: **[Anki decks](vocab/README.md)** per five-lesson block – TSV + import files + packaged decks downloadable from the review lessons, stable GUIDs (re-generating creates no duplicate cards).

## Editorial principles (summary)

- Explanations in **English**; established terminology in English, with the relevant Greek terms in parentheses when needed for reference (*hiatus*, *vocative*, *ablative*…).
- Examples use **English** to make the patterns visible; occasional **Latin comparisons** (the two languages are close relatives).
- Level I vocabulary always comes with a **Latinized transliteration** (e.g. ὁ ἄνθρωπος → *ho ánthrōpos*) so you can read aloud from day one.
- Each lesson: example tables (Greek – transliteration – English), a "Watch out" section for common traps, a summary comparison table at the end, plus exercises with hidden answers (revealed when printing).

Details: [docs/STYLE-AND-CONVENTIONS.md](docs/STYLE-AND-CONVENTIONS.md)

## Copyright policy

All content is **independently compiled**. Only used: grammar/language facts (not copyrightable), **public domain** original texts (ancient authors, classical grammars), and self-written examples/exercises/simplified readings. No copyrighted textbook is stored or copied. Details: [docs/COPYRIGHT.md](docs/COPYRIGHT.md).

## Credit (required when reusing)

All content is compiled by **Trần Quốc Tân** and released free of charge under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). When citing, quoting, translating, reprinting, teaching, or building material on top of this content, you **must give clear credit**:

> Source: **Graecum VN** – compiled by **Trần Quốc Tân**, https://github.com/qtan-tran/graecum-vn, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

This repository is developed and maintained by **Quoc-Tan Tran**, **Postdoctoral Researcher** at the **Institute for Studies of Science, Bielefeld University** *(tiếng Việt: Trần Quốc Tân, nghiên cứu viên tại Institute for Studies of Science, Đại học Bielefeld)*.

If you modify the content, add "with modifications". The same principles apply to commercial, school or translation use. Details: [docs/COPYRIGHT.md](docs/COPYRIGHT.md) section 4.

## Status

| Item | Status |
| --- | --- |
| Architecture + foundation docs | ✅ Part 1 |
| Standard lesson template | ✅ Part 1 |
| Vietnamese Lessons 1–20 + Reviews #1–#3 (Graecum I) | ✅ published |
| Vietnamese Lessons 21–24 + Reviews #4–#5 (rest of Graecum I) | 📋 on the roadmap |
| Graecum II (25–48) | 📋 on the roadmap |
| Vocab TSV + Anki decks (blocks 1–15) | ✅ published |
| Toolkit repo (ancient-greek-toolkit) | ✅ split out, live |
| Sentence-analysis platform (satzanalyse) | 📋 on the roadmap |
| English edition | 🔄 portal + Lessons 1–6 published |

See: [docs/ROADMAP.md](docs/ROADMAP.md)

## Contributing

All contributions are welcome: proofreading, writing exercises, compiling readings, building Anki decks. Start from [docs/ROADMAP.md](docs/ROADMAP.md), [CONTRIBUTING.md](CONTRIBUTING.md) and Issues.
