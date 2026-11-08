def build_statistics_settings(
    st,
    settings
):

    st.sidebar.header(
        "Statistics"
    )

    settings.statistics.method = (

        st.sidebar.selectbox(

            "Test",

            [

                "Auto",

                "Student T-Test",

                "Welch T-Test",

                "Mann-Whitney U",

                "One-Way ANOVA",

                "Kruskal-Wallis"

            ]

        )

    )

    settings.statistics.error_type = (

        st.sidebar.selectbox(

            "Error",

            [

                "SEM",

                "SD"

            ]

        )

    )

    settings.statistics.show_statistics = (

        st.sidebar.checkbox(

            "Display Statistics",

            value=settings.statistics.show_statistics

        )

    )

    return settings