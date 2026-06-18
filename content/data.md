+++
title = "Data"
description = "LSC Data"
weight = 1
+++

# LSC'26 Dataset

The LSC'26 will reuse the same 18 months of the dataset that used in LSC'22/23/24/25, which is available for download. The dataset consists of three password protected files:

* **Core Image Dataset**: Wearable camera images, fully redacted and anonymised in 1024 x 768 resolution, captured using a Narrative Clip device. These images were collected during 2019-2020. All faces and readable text have been removed, as well as certain scenes and activities manually filtered out to respect local privacy requirements.
* **Metadata**: For the collection, consisting of textual metadata representing time and locations, etc.
* **Visual Concepts**: Extracted from the non-redacted version of the visual dataset.


## Supplementary Data

In addition to the official LSC'26 dataset, we recommend the use of the following supplementary resources to enhance retrieval performance:

* **VAISL**: A supplementary metadata file, provided by Tran et al. for the LSC’23 campaign, contains semantic names for lifelogger location (e.g., ‘home’, ‘Dublin City University’, ‘Zurich Airport’, etc.). [Request here](https://huggingface.co/datasets/icmr-lsc/lsc22-25/resolve/main/VAISL_metadata.csv).
* **Additional flight data**: Flight locations as [departing airport, arrival airport] pairs are provided by the Voxento developer, who was also a participant in LSC’23. [Download Link](https://lifelogsearch.org/lsc/resources/airplane_location_label.csv.zip)

Please cite the following papers if you use these:

* Ly-Duyen Tran, Dongyun Nie, Liting Zhou, Binh Nguyen, and Cathal Gurrin. 2023. VAISL: Visual-Aware Identification of Semantic Locations in Lifelog. In MultiMedia Modeling: 29th International Conference, MMM 2023, Bergen, Norway, January 9–12, 2023, Proceedings, Part II. Springer-Verlag, Berlin, Heidelberg, 659–670. [https://doi.org/10.1007/978-3-031-27818-1_54](https://doi.org/10.1007/978-3-031-27818-1_54)
* Ahmed Alateeq, Mark Roantree, and Cathal Gurrin. 2023. Voxento 4.0: A More Flexible Visualisation and Control for Lifelogs. In Proceedings of the 6th Annual ACM Lifelog Search Challenge (LSC '23). Association for Computing Machinery, New York, NY, USA, 7–12. [https://doi.org/10.1145/3592573.3593097](https://doi.org/10.1145/3592573.3593097)


## Access {#access}

> Due to the sensitive nature of the data, access to the LSC'26 dataset is restricted to registered participants who have signed the necessary agreements to ensure ethical use and compliance with data protection regulations.
>
> For access to the dataset, please fill in the following forms:
>
> [LSC2026 Organisation Agreement Form](../documents/LSC2026_Organisation_Agreement_Form.docx)
> * The research team leader must sign this form on behalf of the organisation to which the participants belong. This form should be sent to **both** of the following email addresses: [cathal.gurrin@dcu.ie](mailto:cathal.gurrin@dcu.ie) and [allie.tran@dcu.ie](mailto:allie.tran@dcu.ie).
>
> [LSC2026 Individual Agreement Form](../documents/LSC2026_Individual_Agreement_Form.docx)
> * Every team member who intends to use the LSC data collection must sign an individual agreement. These documents should be kept on file by your own organisation rather than sent to the organisers, unless requested at a later date.
>

The dataset is available at [https://huggingface.co/datasets/icmr-lsc/lsc22-25/](https://huggingface.co/datasets/icmr-lsc/lsc22-25/). Please note that you will need to have the previously mentioned forms completed and submitted to the organisers. Access is granted on a case-by-case basis, and the password to unzip the files will be provided via email.




## Citation

For referencing the LSC'26 dataset in publications, please use the following citation:

```bibtex
@inproceedings{LSC26,
    author = {Gurrin, Cathal and Zhou, Liting and Healy, Graham and Tran, Allie and Rossetto, Luca and Bailer, Werner and Dang-Nguyen, Duc-Tien and Hodges, Steve and \TH{}\'{o}r J\'{o}nsson, Bj\"{o}rn and Tran, Minh-Triet and Sch\"{o}ffmann, Klaus},
    title = {Introduction to the 9th Annual Lifelog Search Challenge, LSC'26},
    year = {2026},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    booktitle = {Proceedings of the 2026 International Conference on Multimedia Retrieval},
    keywords = {benchmarking, interactive retrieval systems, lifelog},
    location = {Amsterdam, Netherlands},
    series = {ICMR '26}
    doi = {10.1145/3805622.3811234}
}

```

# Expanded Dataset for LSC'27

We are in the process of finalising the expanded dataset for LSC'27, which will include additional years of data. A sample of the expanded dataset can be found at [https://huggingface.co/datasets/icmr-lsc/lsc27](https://huggingface.co/datasets/icmr-lsc/lsc27). The same access requirements apply for this.

The final dataset will follow the same structure and is expected to be released in summer 2026.

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

