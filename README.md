# 📰 Fake News Detector

This project is designed to detect fake news using cutting-edge machine learning models! We leverage the power of **transformers** and **Distilled BART** to analyze news articles and classify them as real or fake. The dataset used for training is sourced from Kaggle.

## 🚀 Features
- **Transformer-based architecture**: Using Huggingface's Transformers library.
- **Distilled BART**: Faster and lighter model for NLP tasks.
- **Data from Kaggle**: Pre-processed and ready to use!

---

## 📁 Project Structure

This project follows the [Poetry](https://python-poetry.org/) structure for package management and dependency handling.

---

## 🛠️ How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/penscola/Misinformation-Prediction
   cd fake-news-detector
   ```

2. **Install dependencies**:
   We use Poetry for dependency management. If you don't have it installed, you can install it [here](https://python-poetry.org/docs/#installation).

   ```bash
   poetry install
   ```

3. **Download the Dataset**:
   You can obtain the dataset from Kaggle:
   - [Fake News Dataset](https://www.kaggle.com/)
   Once downloaded, place the dataset in the `data/` directory.

4. **Run the model**:
   You can run the model using the command below:
   ```bash
   poetry run python src/app.py
   ```

5. **Test the model**:
   To run the tests:
   ```bash
   poetry run pytest
   ```

---

## 🤝 How to Contribute

Contributions are always welcome! Here’s how you can get started:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes**.
4. **Commit your changes**:
   ```bash
   git commit -m "Add some new feature"
   ```
5. **Push to the branch**:
   ```bash
   git push origin feature-branch
   ```
6. **Create a pull request** on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
