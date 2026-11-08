# GraphAppV2 Architecture

## Project Vision


GraphAppV2 is a GraphPad Prism-inspired
statistical analysis and scientific
figure generation platform focused on
microbiology and experimental biology.


## Architecture


core/
stats/
annotations/
axes/
graph_types/
themes/
palettes/
ui/
tests/


## Data Models


Grouped Data:

Control | MutA | MutB

Used for:
- Bar
- Box
- Violin
- ANOVA
- T-tests

XY Data:

Time | WT | WT | MutA | MutA

Duplicate column names are treated
as biological replicates.


## Future Features


- Box + Points
- Violin + Points
- True Grouped Bar Plot
- Two-Way ANOVA
- Repeated Measures ANOVA
- Growth Curve Analysis
- PCA
- Volcano Plots
- Tn-Seq Analysis

