+++
title = "Data"
description = "LSC Data"
weight = 1
+++

# LSC'26 Dataset

> LSC'26 will use an **expanded dataset** compared to previous years, featuring four years of rich multimodal lifelog data, including wearable camera images, biometrics, activities, and locations.
> The dataset is currently being finalised and will be made available to registered participants closer to the submission deadline. Check [News](../news/) for updates.

In the meantime, 18 months of the dataset used in LSC'22/23/24/25 is available for download. The dataset consists of three password protected files:

* **Core Image Dataset**: Wearable camera images, fully redacted and anonymised in 1024 x 768 resolution, captured using a Narrative Clip device. These images were collected during 2019-2020. All faces and readable text have been removed, as well as certain scenes and activities manually filtered out to respect local privacy requirements.
* **Metadata**: For the collection, consisting of textual metadata representing time and locations, etc.
* **Visual Concepts**: Extracted from the non-redacted version of the visual dataset.


## Supplementary Data

In addition to the official LSC'26 dataset, we recommend the use of the following supplementary resources to enhance retrieval performance:

* **VAISL**: A supplementary metadata file, provided by Tran et al. for the LSC’23 campaign, contains semantic names for lifelogger location (e.g., ‘home’, ‘Dublin City University’, ‘Zurich Airport’, etc.). [Download Link](https://www.dropbox.com/scl/fi/5m3bz6ixkhchzzo5b3fzd/vaisl_gps.csv)
* **Additional flight data**: Flight locations as [departing airport, arrival airport] pairs are provided by the Voxento developer, who was also a participant in LSC’23. [Download Link](https://lifelogsearch.org/lsc/resources/airplane_location_label.csv.zip)

Please cite the following papers if you use these:

* Ly-Duyen Tran, Dongyun Nie, Liting Zhou, Binh Nguyen, and Cathal Gurrin. 2023. VAISL: Visual-Aware Identification of Semantic Locations in Lifelog. In MultiMedia Modeling: 29th International Conference, MMM 2023, Bergen, Norway, January 9–12, 2023, Proceedings, Part II. Springer-Verlag, Berlin, Heidelberg, 659–670. [https://doi.org/10.1007/978-3-031-27818-1_54](https://doi.org/10.1007/978-3-031-27818-1_54)
* Ahmed Alateeq, Mark Roantree, and Cathal Gurrin. 2023. Voxento 4.0: A More Flexible Visualisation and Control for Lifelogs. In Proceedings of the 6th Annual ACM Lifelog Search Challenge (LSC '23). Association for Computing Machinery, New York, NY, USA, 7–12. [https://doi.org/10.1145/3592573.3593097](https://doi.org/10.1145/3592573.3593097)


## Access

> For access to the full dataset, please email either:
> * cathal.gurrin@dcu.ie
> * allie.tran@dcu.ie
>
>

## Citation

For referencing the LSC'26 dataset in publications, please use the following citation:

```bibtex
@inproceedings{LSC26,
    author = {Gurrin, Cathal and Zhou, Liting and Healy, Graham and Tran, Allie and Rossetto, Luca and Bailer, Werner and Dang-Nguyen, Duc-Tien and Hodges, Steve and \TH{}\'{o}r J\'{o}nsson, Bj\"{o}rn and Tran, Minh-Triet and Sch\"{o}ffmann, Klaus},
    title = {Introduction to the 8th Annual Lifelog Search Challenge, LSC'26},
    year = {2026},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    booktitle = {Proceedings of the 2026 International Conference on Multimedia Retrieval},
    keywords = {benchmarking, interactive retrieval systems, lifelog},
    location = {Amsterdam, Netherlands},
    series = {ICMR '26}
}

```

---

# Topics in Previous Years

To assist with system development and testing, we provide the topics from previous years of the Lifelog Search Challenge.

* [LSC'25 Topics (Word Document)](../resources/LSC2025-Topics-Release.docx)
* [LSC'24 Topics (PDF)](../resources/LSC24-Topics-Release.pdf)
* [LSC'23 Topics (Text File)](../resources/LSC23-Topics.txt)
* [LSC'22 Topics (Text File)](../resources/lsc22-topics-qrels-shared.txt)
* [LSC'21 Topics (Text File)](../resources/lsc21-topics-qrels-shared.txt)
* [LSC'20 Topics (Text File)](../resources/lsc20-topics-qrels.txt)
* [LSC'19 Topics (XML File)](../resources/lsc2019-topics.xml)
* [LSC'18 Topics (XML File)](../resources/LSC2018_dev_topics.xml)

