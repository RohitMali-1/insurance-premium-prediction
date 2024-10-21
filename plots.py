import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    data = pd.read_csv("data/insurance_c.csv")
    return data

df = load_data()

def create_subplots(n_cols):
    if n_cols == 1:
        fig, ax = plt.subplots(figsize=(16, 7))
        axes = [ax]  
    else:
        fig, axes = plt.subplots(1, n_cols, figsize=(16, 7))
    return fig, axes

# Helper function for countplots
def plot_countplots(df, columns, rotation_cols=[]):
    fig, axes = create_subplots(len(columns))
    
    for ax, col in zip(axes, columns):
        sns.countplot(data=df, x=col, ax=ax)
        if col in rotation_cols:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        if col != columns[0]: 
            ax.set_ylabel('')
    
    plt.tight_layout()
    st.pyplot(fig)

# Helper function for pie charts
def plot_piecharts(df, pie_data):
    fig, axes = plt.subplots(1, 4, figsize=(16, 8))
    for ax, (col, labels, colors) in zip(axes, pie_data):
        size = df[col].value_counts()
        ax.pie(size, colors=colors, labels=labels, autopct='%.2f%%')
        ax.set_title(col.capitalize(), fontsize=20)
        ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)

# Helper function for histograms
def plot_histograms(df, columns):
    fig, axes = create_subplots(len(columns))
    
    for ax, col in zip(axes, columns):
        sns.histplot(data=df, x=col, ax=ax)
        ax.set_title(col.capitalize())
    
    plt.tight_layout()
    st.pyplot(fig)

# KDE plot function
def plot_kde(df, columns, x=None, hue_columns=None):
    fig, axes = create_subplots(len(columns))
    
    for ax, col in zip(axes, columns):
        if hue_columns:
            sns.kdeplot(data=df, x=x, hue=col, ax=ax)
        else:
            sns.kdeplot(data=df, x=col, ax=ax)
        
        ax.grid(True)
        ax.set_title(col.capitalize())
        if col == 'region':
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        if col != columns[0]:
            ax.set_ylabel('') 

    plt.tight_layout()
    st.pyplot(fig)

# Boxplot function
def plot_boxplots(df, columns, y=None, hue=None):
    fig, axes = create_subplots(len(columns))
    
    for ax, col in zip(axes, columns):
        if y:
            sns.boxplot(data=df, x=col, y=y, hue=hue, ax=ax)
        else:
            sns.boxplot(data=df, x=col, ax=ax)
        
        if col == 'region':
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        if col != columns[0]:
            ax.set_ylabel('')  # Remove y-label for all except the first plot

    plt.tight_layout()
    st.pyplot(fig)

# Scatterplot function
def plot_scatter(df, cols_x, cols_y, hue=None):
    fig, axes = create_subplots(len(cols_x))
    
    for ax, (x_col, y_col) in zip(axes, zip(cols_x, cols_y)):
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, ax=ax)
        ax.grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)

# Barplot function
def plot_barplots(df, columns, y, hue=None, rotation_cols=[]):
    fig, axes = create_subplots(len(columns))
    
    for ax, col in zip(axes, columns):
        sns.barplot(data=df, x=col, y=y, hue=hue, ax=ax,errorbar=None)
        
        if col in rotation_cols:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        if col != columns[0]: 
            ax.set_ylabel('')
    
    plt.tight_layout()
    st.pyplot(fig)

# Heatmap function
def plot_heatmap(df, row_col, col_col):
    cross_tab = pd.crosstab(df[row_col], df[col_col])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(cross_tab, annot=True, cmap="Blues", fmt="d", ax=ax)
    st.pyplot(fig)


def univariate_analysis():
    st.write("## Univariate Analysis")

    # Countplot
    st.write("### Countplot")
    plot_countplots(df, ["sex", "smoker", "region", "children"], rotation_cols=["region"])

    # Pie Chart
    st.write("### Pie Chart")
    pie_data = [
        ('sex', ['Male', 'Female'], ['red', 'green']),
        ('smoker', ['No', 'Yes'], ['red', 'green']),
        ('region', ['southeast', 'southwest', 'northwest', 'northeast'], ['red', 'green', 'blue', 'cyan']),
        ('children', ['0', '1', '2', '3', '4', '5'], ['red', 'green', 'blue', 'cyan', 'yellow', 'orange'])
    ]
    plot_piecharts(df, pie_data)

    # Histogram
    st.write("### Histogram")
    plot_histograms(df, ['age', 'bmi', 'charges'])

    # KDE Plot
    st.write("### KDE Plot")
    plot_kde(df, ['age', 'bmi', 'charges'])

    # Boxplot
    st.write("### Boxplot")
    plot_boxplots(df, ['age', 'bmi', 'charges'])

def bivariate_analysis():
    st.write("## Bivariate Analysis")

    # Scatter Plot
    st.write("### Scatter Plot")
    plot_scatter(df, ['bmi', 'age'], ['charges', 'charges'])

    # Bar Plot
    st.write("### Bar Plot")
    plot_barplots(df, ['sex', 'smoker', 'region', 'children'], y="charges")

    # Box Plot
    st.write("### Box Plot")
    plot_boxplots(df, ['sex', 'smoker', 'region', 'children'], y="charges", hue='smoker')

    # KDE Plot
    st.write("### KDE Plot")
    plot_kde(df, ['sex', 'smoker', 'region', 'children'], x='charges', hue_columns=['sex', 'smoker', 'region', 'children'])

    # Heat Map
    st.write("### Heat Map")
    plot_heatmap(df, "region", "smoker")

def multivariate_analysis():
    st.write("## Multivariate Analysis")
    st.write("### Scatter Plot")
    plot_scatter(df, ['bmi', 'age'], ['charges', 'charges'], hue='smoker')

    # Count Plot
    st.write("### Bar Plot")
    plot_barplots(df, ['sex', 'region', 'children'], y="charges", hue="smoker", rotation_cols=["region"])