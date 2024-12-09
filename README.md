# **NLP Final Project: Evaluating Sign Language Generation Using Embedding-Based Metrics**

## **Overview**

This project focuses on the **Production/Generation** aspect of **Sign Language Processing (SLP)**. While **Natural Language Processing (NLP)** has seen significant advances, SLP remains underexplored due to its multimodal complexities. Traditional evaluation methods for sign language generation rely on **n-gram-based metrics** like **BLEU** and **ROUGE**, which fail to capture the full semantics and pragmatics of sign language.  

Our project investigates the effectiveness of **embedding-based evaluation methods**, specifically **SignScore**, which leverages contrastive learning. The results suggest that embedding-based approaches outperform traditional metrics, providing a more accurate evaluation of sign language generation.

## **Key Findings**

- **Embedding-based metrics (SignScore)** demonstrate superior performance in capturing semantic and pragmatic features compared to traditional n-gram-based metrics.
- SignScore shows **robustness to prosodic variations** (e.g., facial expressions, pauses) that traditional methods fail to capture.
- The **kernel density plots** and **statistical tests** confirm SignScore's ability to distinguish between aligned and misaligned video-text pairs effectively.

## **Project Structure**

```plaintext
NLP-final-project/
│
├── signscore/
│   └── statistical_testing.ipynb       # Statistical testing for SignScore
│
├── MSKA/
│   └── MSKA_results/                   # Kernel Density Plot for traditional n-gram-based metrics
│
├── CiCo/
│   └── CLCL/
│       ├── results.ipynb               # Kernel Density Plot for embedding-based metrics
│       └── prosody.ipynb               # Box plots and correlation testing for prosody analysis
│
├── README.md                           # Project documentation
└── requirements.txt                    # Dependencies
```
## **Installation**
To set up the project, follow these steps:
1. **Clone the repository:**

   ```bash
   git clone git@github.com:sakimai/NLP-final-project.git
   cd NLP-final-project
   ```

## **Usage**
To run the notebooks and explore the results, use Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## **Notebooks to Explore**
- SignScore and Statistical Testing:
Open signscore/statistical_testing.ipynb to run statistical tests comparing SignScore to traditional metrics.

- Kernel Density Plots for N-gram Metrics:
Explore the distribution of scores in MSKA/MSKA_results.

- Kernel Density Plots for Embedding Metrics:
Open CiCo/CLCL/results.ipynb for visual comparisons of embedding-based metrics.

- Prosody Analysis:
Analyze the robustness of SignScore to prosodic variations using CiCo/CLCL/prosody.ipynb.

## **Key Technologies**
- Python 3.8
- Jupyter Notebook
- scikit-learn
- Matplotlib
- Transformers (HuggingFace)
- NumPy
- Pandas
