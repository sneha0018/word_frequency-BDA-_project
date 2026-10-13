# Word Frequency Analysis Using MapReduce

A web-based Big Data Analytics (BDA) mini project that analyzes text data and calculates the frequency of individual words using the MapReduce processing model.

## 📌 Project Overview

Word Frequency Analysis is a text analytics application that counts how many times each word appears in a given text document. It uses three processing stages: **Map, Shuffle and Sort, and Reduce**.

The application provides a user-friendly web dashboard where users can enter text or upload a `.txt` file and view the analysis results through summary cards, a searchable frequency table, and a bar chart.

## 🎯 Objectives

- Implement the MapReduce processing model for word frequency analysis.
- Extract words and generate key-value pairs.
- Group identical words and calculate their frequencies.
- Visualize the results using tables and charts.
- Provide an interactive web interface for text analysis.
- Measure the approximate processing time.

## ✨ Features

- **Text Input:** Enter text directly into the application.
- **File Upload:** Upload `.txt` files for analysis.
- **Map Phase:** Convert each word into a `(word, 1)` key-value pair.
- **Shuffle and Sort:** Group identical words together.
- **Reduce Phase:** Calculate the total frequency of each word.
- **Summary Dashboard:** Display total words, unique words, most frequent word, and processing time.
- **Searchable Results:** Search for specific words in the frequency table.
- **Data Visualization:** Display word frequencies using a bar chart.
- **Responsive UI:** Access the dashboard on desktop and mobile-sized screens.

## 🛠️ Technologies Used

| Technology          | Purpose                                     |
| ------------------- | ------------------------------------------- |
| Python              | Core programming and text processing        |
| Flask               | Backend web framework                       |
| HTML5               | Frontend structure                          |
| CSS3                | Styling and responsive layout               |
| JavaScript          | Frontend interactions and API communication |
| Chart.js            | Bar-chart visualization                     |
| Regular Expressions | Word extraction and punctuation handling    |

## 🏗️ System Architecture

```text
              User
               |
               v
       Web Dashboard
     (HTML, CSS, JavaScript)
               |
               v
       Flask Backend
          /analyze
               |
               v
         Map Phase
       (word, 1) pairs
               |
               v
     Shuffle and Sort
      (group by word)
               |
               v
         Reduce Phase
      (sum frequencies)
               |
               v
         JSON Response
               |
               v
     Results Dashboard
    Table + Bar Chart
```

## ⚙️ How MapReduce Works

### 1. Map Phase

The input text is converted into lowercase, and individual words are extracted. Each word is represented as a key-value pair.

**Example input:**

```text
Big data is useful. Big data is powerful.
```

**Mapper output:**

```text
(big, 1)
(data, 1)
(is, 1)
(useful, 1)
(big, 1)
(data, 1)
(is, 1)
(powerful, 1)
```

### 2. Shuffle and Sort Phase

Identical words are grouped together with their corresponding values.

```text
big      -> [1, 1]
data     -> [1, 1]
is       -> [1, 1]
useful   -> [1]
powerful -> [1]
```

### 3. Reduce Phase

The values associated with each word are added to calculate the final frequency.

```text
big      -> 2
data     -> 2
is       -> 2
useful   -> 1
powerful -> 1
```

The final results are sorted by descending frequency.

## 📂 Project Structure

```text
word_frequenct(BDA)/
│
├── app.py
├── input.txt
├── word_frequency.py
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

**File descriptions:**

- `app.py` — Flask application, API endpoint, and MapReduce functions.
- `input.txt` — Optional sample text file.
- `word_frequency.py` — Optional standalone word-frequency implementation.
- `templates/index.html` — Dashboard interface and JavaScript.
- `static/style.css` — Dashboard styling and responsive design.
- `README.md` — Project documentation.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or later recommended.
- pip package manager.
- Visual Studio Code or another code editor.
- Internet connection for loading Chart.js from its CDN.

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Alternatively, download the repository and open its folder in VS Code.

### Step 2: Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
python -m pip install flask
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the dashboard

Open the following URL in your web browser:

```text
http://127.0.0.1:5000
```

The dashboard will load, and you can enter text or upload a `.txt` file to begin analyzing word frequencies.

## 🧪 Sample Input and Output

**Input:**

```text
Big data is useful. Big data is powerful.
```

**Expected output:**

| Word     | Frequency |
| -------- | --------: |
| big      |         2 |
| data     |         2 |
| is       |         2 |
| useful   |         1 |
| powerful |         1 |

**Summary:**

- Total Words: 8
- Unique Words: 5
- Highest Frequency: 2

The dashboard displays the calculated frequencies in a table and a bar chart.

## 📊 Complexity Analysis

Let `N` represent the total number of words and `U` represent the number of unique words.

- Mapping: `O(N)`
- Grouping: `O(N)` expected
- Reducing: `O(N)`
- Sorting: `O(U log U)`
- Overall Time Complexity: `O(N + U log U)`
- Space Complexity: `O(N + U)`

These estimates apply to the current in-memory Python implementation.

## 🔮 Future Enhancements

- Integrate Hadoop MapReduce and HDFS.
- Support distributed processing across multiple machines.
- Add stop-word removal and advanced text preprocessing.
- Support additional file formats such as CSV and PDF.
- Add CSV export functionality.
- Implement word-cloud visualization.
- Store analysis history in a database.
- Improve performance for large datasets.

## ⚠️ Limitations

- The current implementation executes MapReduce stages locally in a single Python process.
- It does not currently use a Hadoop cluster or distributed worker nodes.
- Large inputs may require substantial memory.
- Word extraction is primarily designed for English alphanumeric text.
- Analysis history is not stored in a database.

## 🎓 Academic Information

**Subject:** Big Data Analytics (BDA)

**Project:** Word Frequency Analysis Using MapReduce

**Project Type:** Web-based text analytics mini project

## 📝 Conclusion

This project demonstrates how the MapReduce processing model can be used to analyze text and calculate word frequencies. By combining Python, Flask, HTML, CSS, JavaScript, and Chart.js, it provides an interactive dashboard for processing text and visualizing the results.

The project offers practical experience with text preprocessing, key-value pairs, grouping, aggregation, backend API development, and data visualization.

## 👩‍💻 Author

Add the project team members' names here.

## 📄 License

This project is developed for academic and educational purposes.
