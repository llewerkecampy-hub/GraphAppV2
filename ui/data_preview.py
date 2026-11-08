# ui/data_preview.py


def show_data_preview(
    st,
    dataframe
):

    st.subheader(
        "Data Preview"
    )

    st.dataframe(
        dataframe
    )

    st.write(
        f"Rows: {len(dataframe)}"
    )

    st.write(
        f"Columns: {len(dataframe.columns)}"
    )