# core/data_manager.py

import pandas as pd
import numpy as np


# =====================================================
# File Loading
# =====================================================

def load_file(file):

    name = file.name.lower()

    if name.endswith(".csv"):

        return clean_dataframe(
            pd.read_csv(file)
        )

    if name.endswith(
        (".xlsx", ".xls")
    ):

        return clean_dataframe(
            pd.read_excel(file)
        )

    raise ValueError(
        "Unsupported file type"
    )



# =====================================================
# Cleaning
# =====================================================

def clean_dataframe(df):

    df = df.copy()

    # Remove Excel unnamed columns

    df = df.loc[
        :,
        ~df.columns.astype(str)
        .str.contains("^Unnamed")
    ]

    return df


# =====================================================
# Validation
# =====================================================

def validate_dataframe(df):

    if df is None:

        raise ValueError(
            "DataFrame is None."
        )

    if df.empty:

        raise ValueError(
            "DataFrame contains no data."
        )

    if len(df.columns) < 1:

        raise ValueError(
            "No columns detected."
        )

    return True


# =====================================================
# Data Type Detection
# =====================================================

def detect_data_type(
    df,
    graph_type
):

    if graph_type in [

        "Line",
        "Scatter"

    ]:

        return "XY"

    return "Grouped"


# =====================================================
# Column Helpers
# =====================================================

def get_column_names(df):

    return list(
        df.columns
    )


def get_group_names(df):

    return list(
        df.columns
    )


# =====================================================
# GROUPED DATA
# Used by:
# Bar
# Box
# Violin
# Dot
# Swarm
# Strip
# =====================================================

def get_grouped_data(df):

    groups = {}

    for column in df.columns:

        groups[column] = (
            df[column]
            .dropna()
            .tolist()
        )

    return groups


def grouped_to_long_format(df):

    frames = []

    for column in df.columns:

        temp = pd.DataFrame(
            {
                "Group": column,
                "Value": df[column].dropna()
            }
        )

        frames.append(temp)

    return pd.concat(
        frames,
        ignore_index=True
    )


# =====================================================
# XY DATA
# Used by:
# Scatter
# Line
# Growth Curves
# Time Course
# =====================================================

def get_xy_data(df):

    if len(df.columns) < 2:

        raise ValueError(
            "XY data requires at least "
            "one X column and one Y column."
        )

    x_column = df.columns[0]

    x_values = (
        df.iloc[:, 0]
        .tolist()
    )

    conditions = {}

    # Handle duplicate column names correctly

    for i in range(
        1,
        len(df.columns)
    ):

        condition_name = (
            normalize_xy_column_name(
                df.columns[i]
            )
        )

        y_values = (
            df.iloc[:, i]
            .tolist()
        )

        if condition_name not in conditions:

            conditions[
                condition_name
            ] = []

        conditions[
            condition_name
        ].append(
            y_values
        )
    

    return {

        "x_label":
        x_column,

        "x_values":
        x_values,

        "conditions":
        conditions
    }


# =====================================================
# XY SUMMARY
# =====================================================

def summarize_xy_condition(
    replicate_list
):

    arr = np.array(
        replicate_list,
        dtype=float
    )

    means = np.mean(
        arr,
        axis=0
    )

    sem = (

        np.std(
            arr,
            axis=0,
            ddof=1
        )

        /

        np.sqrt(
            arr.shape[0]
        )

    )

    return {

        "mean": means,

        "sem": sem
    }


def summarize_xy_data(
    xy_data
):

    summaries = {}

    conditions = (
        xy_data["conditions"]
    )

    for name, replicates in (
        conditions.items()
    ):

        summaries[name] = (
            summarize_xy_condition(
                replicates
            )
        )

    return summaries


# =====================================================
# Replicate Helpers
# =====================================================

def get_replicate_count(
    xy_data,
    condition_name
):

    return len(

        xy_data[
            "conditions"
        ][
            condition_name
        ]

    )


def get_condition_names(
    xy_data
):

    return list(

        xy_data[
            "conditions"
        ].keys()

    )


# =====================================================
# Statistics Helpers
# =====================================================

def calculate_means(df):

    return df.mean(
        numeric_only=True
    )


def calculate_sd(df):

    return df.std(
        numeric_only=True
    )


def calculate_sem(df):

    return (

        df.std(
            numeric_only=True
        )

        /

        np.sqrt(
            df.count()
        )

    )


# =====================================================
# Graph Helpers
# =====================================================

def determine_error_values(
    df,
    error_type
):

    if error_type == "SEM":

        return calculate_sem(df)

    if error_type == "SD":

        return calculate_sd(df)

    raise ValueError(
        f"Unsupported error type: "
        f"{error_type}"
    )


# =====================================================
# Metadata
# =====================================================

def describe_dataset(
    df
):

    return {

        "rows":
        len(df),

        "columns":
        len(df.columns),

        "column_names":
        list(df.columns)
    }

# =====================================================
# Column Name Normalization
# =====================================================

def normalize_xy_column_name(
    name
):

    name = str(name)

    if "." in name:

        prefix = name.split(".")[0]

        suffix = name.split(".")[-1]

        if suffix.isdigit():

            return prefix

    return name