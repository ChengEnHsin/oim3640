# Text Mining Project: Comparing Classic Literature

# Overview

In this project, I analyzed three classic novels: Little Women, Pride and Prejudice, and The Brothers Karamazov (with an additional comparison to Dracula).

The goal was to understand how different authors use language by applying text mining techniques such as word frequency analysis, TF-IDF, and vocabulary richness.


# What I Did

I cleaned and processed each text by converting everything to lowercase, removing punctuation, and splitting the text into words. Then I computed word frequencies, vocabulary size, and TF-IDF scores to identify distinctive words in each book. 

I also created visualizations including:

* Bar charts of the most common words in each book
* A comparison chart of vocabulary richness across books

One thing I found especially interesting was applying TF-IDF, since I was introduced to it last semester in my machine learning class at Babson. Before, I understood it more conceptually, but this project helped me see how it actually works in practice to highlight words that are important within one text but not across all texts.


# Questions I Explored

1. Which words are uniquely important to each book?
2. How does word usage differ across authors?
3. How often do key themes like “love,” “family,” “faith,” and “money” appear?
4. Which book uses the most repetitive language?
5. How concentrated are the most common words in each text?


# Key Findings

1. Each book has a distinct “voice”

Using TF-IDF, I found that each book has its own set of highly distinctive words. This shows that even though all texts are written in English, the authors emphasize very different ideas and contexts.

* *Little Women* highlights domestic and family-centered language
* *Pride and Prejudice* emphasizes social relationships and dialogue
* *The Brothers Karamazov* focuses more on philosophical and religious terms


2. Vocabulary richness varies across authors

By comparing the ratio of unique words to total words, I found clear differences in writing style.

* Dostoevsky’s writing tends to be more complex and diverse
* Austen’s writing is more structured and consistent
* Alcott falls somewhere in between, balancing narrative and dialogue

This suggests that more philosophical texts tend to use a wider range of vocabulary.


3. Themes show up differently across books

When analyzing keywords like “love,” “family,” “faith,” and “money,” I saw clear thematic differences:

* “Family” appears more frequently in *Little Women*
* “Love” and social terms appear more in *Pride and Prejudice*
* “Faith” appears more often in *The Brothers Karamazov*

This confirms the known themes of each novel through data, not just interpretation.


4. Repetitiveness reveals writing style

By measuring vocabulary diversity, I found that some books reuse words more than others.

* More repetitive texts tend to focus tightly on specific topics or dialogue
* Less repetitive texts explore broader or more abstract ideas

This helps quantify something that is usually subjective in literary analysis.

 5. Common words dominate a large portion of text

A small number of high-frequency words make up a large percentage of each book.

This shows how language follows a predictable pattern (Zipf’s Law), where a few words are used very often while most words are rare.


# What Surprised Me

One of the most surprising findings was how clearly data could reflect themes that we usually think of as purely “literary.”

For example, without reading the books, the model could still identify that:

*Little Women* is family-oriented
*Pride and Prejudice* is socially focused
*The Brothers Karamazov* is philosophical

It was also interesting to connect this back to what I learned in class. Concepts like TF-IDF that I previously saw in a machine learning context became much more intuitive when I applied them to real text and could directly interpret the results.



# Conclusion

This project shows that text mining can reveal meaningful insights about literature. By combining simple preprocessing with techniques like TF-IDF and frequency analysis, I was able to compare writing styles, themes, and language patterns across multiple books.

Overall, this project demonstrates how data analysis can complement traditional reading by providing a more quantitative perspective on texts.


# Milestone Approach and Reflection

For Milestones 1 and 2, I completed the core parts of this project using only built-in Python concepts such as strings, lists, dictionaries, sets, and file I/O. This meant I manually cleaned the text, split it into words, tracked frequencies, and compared vocabulary across books without relying on external libraries. Doing it this way helped me understand what is actually happening behind text analysis instead of just calling a function and accepting the output.

Working through the analysis the hard way made me think more carefully about each step. I had to decide how to remove punctuation, how to structure word counts using dictionaries, and how to calculate metrics like vocabulary richness meanwhile giving AI the right instrutions to ensure accuracy. This process made the logic much clearer and reinforced the core programming concepts we have been learning in class.

After completing the foundational analysis, I expanded the project by incorporating tools like matplotlib for visualization and more advanced techniques such as TF-IDF. These additions are reflected in my later code, where I move beyond basic Python to generate charts and highlight important words across texts. This progression shows how the project evolved from foundational implementation to more advanced analysis. 

Comparing the two approaches, using libraries was significantly faster and made it easier to produce clean visualizations and more advanced insights. However, starting with built-in Python was more valuable for learning. It gave me a clear understanding of how the data is processed step by step, which made the library-based approach feel much more intuitive rather than like a black box.

One especially meaningful connection for me was TF-IDF. I was introduced to TF-IDF last semester in my machine learning class at Babson, but this project helped me truly understand how it works in practice. Beyond TF-IDF, the overall text cleaning and mining process also felt familiar because I had learned similar workflows in that class. What made this project interesting was applying those same concepts in a different environment. In my machine learning course, I used RStudio, so working in VS Code with Python gave me a new perspective on how the same ideas translate across tools and languages.

Overall, this project showed me that while libraries are powerful for efficiency and presentation, doing the analysis manually first builds a much stronger foundation. It made the transition to more advanced tools smoother and helped me better interpret and explain my results.



