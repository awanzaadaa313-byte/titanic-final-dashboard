import matplotlib.pyplot as plt
import seaborn as sns

# Global styling to perfectly sync with Streamlit's dark mode theme
def apply_chart_style(fig, ax, title, xlabel="", ylabel=""):
    # Using Streamlit's exact dark background color so charts blend seamlessly
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#161b22')
    
    # Elegant title configuration
    ax.set_title(title, fontsize=13, fontweight='bold', pad=15, color='#56cfe1')
    
    # Beautiful muted gray axes labels
    if xlabel: ax.set_xlabel(xlabel, fontsize=10, color='#8b949e', labelpad=8)
    if ylabel: ax.set_ylabel(ylabel, fontsize=10, color='#8b949e', labelpad=8)
    
    # Ticks adjustment
    ax.tick_params(colors='#8b949e', labelsize=9)
    
    # Subtle dark grid lines
    ax.grid(True, linestyle=':', alpha=0.15, color='#ffffff')
    
    # Clean up ugly borders completely
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    fig.tight_layout()

# 1. Class-wise Average Fare (Neon Blue Gradient Bars)
def draw_bar_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        colors = ['#1f77b4', '#4ea8de', '#72efdd']
        sns.barplot(data=df, x='pclass', y='fare', ax=ax, palette=colors, errorbar=None, edgecolor='#161b22', linewidth=1.5)
    apply_chart_style(fig, ax, 'Class-wise Average Fare', 'Ticket Class', 'Average Fare')
    return fig

# 2. Survival Rate Status (Clean Modern Donut Chart)
def draw_pie_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty and 'survived' in df.columns:
        counts = df['survived'].value_counts()
        colors = ['#ff6b6b', '#2a9d8f']
        labels = ['Deceased', 'Survived']
        
        wedges, texts, autotexts = ax.pie(
            counts, autopct='%1.1f%%', startangle=90, 
            colors=colors, labels=labels, 
            textprops=dict(color="#ffffff", weight="bold", fontsize=10),
            wedgeprops=dict(width=0.45, edgecolor='#0e1117', linewidth=3)
        )
        for text in texts:
            text.set_color('#8b949e')
    apply_chart_style(fig, ax, 'Survival Rate Status')
    return fig

# 3. Age Distribution of Passengers (Smooth Density Histogram)
def draw_age_dist(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.histplot(data=df, x='age', bins=20, kde=True, ax=ax, color='#b5179e', alpha=0.5, edgecolor='#ffffff', linewidth=0.3)
        if ax.lines:
            ax.lines[0].set_color('#f72585')
            ax.lines[0].set_linewidth(2)
    apply_chart_style(fig, ax, 'Age Distribution of Passengers', 'Passenger Age', 'Count')
    return fig

# 4. Fare vs Age (Glowing Scatter Plot)
def draw_scatter_fare_age(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.scatterplot(data=df, x='age', y='fare', hue='survived', ax=ax, palette=['#ff6b6b', '#2a9d8f'], alpha=0.75, edgecolor='#161b22', s=45)
        legend = ax.legend(title='Status', facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
        plt.setp(legend.get_title(), color='#ffffff')
    apply_chart_style(fig, ax, 'Passenger Fare vs Age', 'Age', 'Fare')
    return fig

# 5. Survival Count by Gender (Side-by-Side Count Plot)
def draw_gender_survival(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='sex', hue='survived', ax=ax, palette=['#ff6b6b', '#2a9d8f'], edgecolor='#161b22', linewidth=1)
        legend = ax.legend(labels=['Deceased', 'Survived'], facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    apply_chart_style(fig, ax, 'Survival Count by Gender', 'Gender', 'Count')
    return fig

# 6. Passenger Count by Embarkation Port (Warm Palette)
def draw_embark_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty and 'embarked' in df.columns:
        sns.countplot(data=df, x='embarked', ax=ax, palette=['#e63946', '#f4a261', '#e9c46a'], edgecolor='#161b22', linewidth=1)
    apply_chart_style(fig, ax, 'Passengers per Embarkation Port', 'Port of Embarkation', 'Count')
    return fig

# 7. Fare Distribution by Passenger Class (Box Plot)
def draw_fare_box(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.boxplot(data=df, x='pclass', y='fare', ax=ax, palette=['#1f77b4', '#4ea8de', '#72efdd'], fliersize=2, boxprops=dict(alpha=0.75))
    apply_chart_style(fig, ax, 'Fare Distribution by Class', 'Ticket Class', 'Fare')
    return fig

# 8. Age vs Class by Survival (Violin Plot)
def draw_age_violin(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.violinplot(data=df, x='pclass', y='age', hue='survived', split=True, ax=ax, palette=['#ff6b6b', '#2a9d8f'], inner="quart", linewidth=1)
        legend = ax.legend(facecolor='#0e1117', edgecolor='none')
        plt.setp(legend.get_texts(), color='#8b949e')
    apply_chart_style(fig, ax, 'Age Distribution by Class & Survival', 'Ticket Class', 'Age')
    return fig

# 9. Siblings/Spouses Aboard Count (Flat Golden Bar)
def draw_sibsp_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='sibsp', ax=ax, color='#e9c46a', alpha=0.8, edgecolor='#161b22')
    apply_chart_style(fig, ax, 'Number of Siblings/Spouses Aboard', 'SibSp Count', 'Passenger Count')
    return fig

# 10. Parents/Children Aboard Count (Flat Emerald Bar)
def draw_parch_count(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    if not df.empty:
        sns.countplot(data=df, x='parch', ax=ax, color='#2a9d8f', alpha=0.8, edgecolor='#161b22')
    apply_chart_style(fig, ax, 'Number of Parents/Children Aboard', 'Parch Count', 'Passenger Count')
    return fig