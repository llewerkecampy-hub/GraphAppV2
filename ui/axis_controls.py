def build_axis_settings(
    st,
    settings
):

    st.sidebar.header(
        "Axis"
    )

    settings.axis.scale = (

        st.sidebar.selectbox(

            "Scale",

            [
                "Linear",
                "Log10",
                "Log2",
                "Natural Log"
            ]

        )

    )

    settings.axis.auto_scale = (

        st.sidebar.checkbox(

            "Auto Scale",

            value=settings.axis.auto_scale

        )

    )

    if not settings.axis.auto_scale:

        settings.axis.y_min = (

            st.sidebar.number_input(
                "Y Min",
                value=float(
                    settings.axis.y_min or 0
                )
            )

        )

        settings.axis.y_max = (

            st.sidebar.number_input(
                "Y Max",
                value=float(
                    settings.axis.y_max or 100
                )
            )

        )

        settings.axis.major_tick_step = (

            st.sidebar.number_input(

                "Major Tick Step",

                value=float(
                    settings.axis.major_tick_step
                )

            )

        )

    st.sidebar.subheader(
        "Tick Controls"
    )

    settings.axis.tick_direction = (

        st.sidebar.selectbox(

            "Tick Direction",

            [
                "out",
                "in",
                "inout"
            ]

        )

    )

    settings.axis.major_tick_length = (

        st.sidebar.slider(

            "Major Tick Length",

            1.0,
            20.0,

            float(
                settings.axis.major_tick_length
            )

        )

    )

    settings.axis.major_tick_width = (

        st.sidebar.slider(

            "Major Tick Width",

            0.5,
            5.0,

            float(
                settings.axis.major_tick_width
            )

        )

    )

    settings.axis.show_minor_ticks = (

        st.sidebar.checkbox(

            "Show Minor Ticks",

            value=settings.axis.show_minor_ticks

        )

    )

    if settings.axis.show_minor_ticks:

        settings.axis.minor_tick_length = (

            st.sidebar.slider(

                "Minor Tick Length",

                1.0,
                15.0,

                float(
                    settings.axis.minor_tick_length
                )

            )

        )

        settings.axis.minor_tick_width = (

            st.sidebar.slider(

                "Minor Tick Width",

                0.1,
                5.0,

                float(
                    settings.axis.minor_tick_width
                )

            )

        )

        settings.axis.minor_divisions = (

            st.sidebar.slider(

                "Minor Tick Divisions",

                1,
                10,

                settings.axis.minor_divisions

            )

        )

    return settings