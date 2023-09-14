# Identifying-COVID-19-Diseases-In-Chest-X-Rays

<p align="center">
  <img src="./reports/demo.png" alt="Demo Image">
</p>

## Table Content
- [Datasets](#datasets)
- [Getting Started](#getting-started)
- [Author](#author)

## Datasets

## Project structure
```
.
├── data
│   ├── train
│   ├── val
│   └── test
├── notebooks
│   └── xception.ipynb
├── reports
│   ├── confusion_matrix.png
│   ├── demo.png
│   ├── model_output.png
│   └── normalized_confusion_matrix.png
└── src
|   ├── api
|   │   ├── 2023-09-02_xception.h5
|   │   ├── 2023-09-02_xception.h5.dvc
|   │   └── main.py
|   ├── models
|   │   ├── 2023-09-02_xception.h5
|   │   └── 2023-09-02_xception.h5.dvc
|   ├── Docker
|   ├── requirements
|   └── train_test_split.py
├── LICENCE
└── README.md
```

## Getting Started
Follow theses steps to set up the environment and run the application.
1. Fork the repository [here](https://github.com/ldebele/Identifying-COVID-19-Diseases-In-Chest-X-Rays.git).
2. Clone the forked repository.
    ```bash
    git clone https://github.com/<YOUR-USERNAME>/Identifying-COVID-19-Diseases-In-Chest-X-Rays.git
    cd Identifying-COVID-19-Diseases-In-Chest-X-Rays.git
    ```
3. Run the application.
    ```bash
    docker-compose up
    ```
## Author
- `Lemi Debela`