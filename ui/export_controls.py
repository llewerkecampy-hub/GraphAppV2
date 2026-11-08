def build_export_settings(
    st,
    settings
):

    st.sidebar.header(
        "Export"
    )

    settings.export.file_format = (

        st.sidebar.selectbox(

            "Format",

            [

                "png",

                "svg",

                "pdf",

                "tiff"

            ]

        )

    )

    settings.export.dpi = (

        st.sidebar.selectbox(

            "DPI",

            [

                300,

                600,

                1200

            ],

            index=1

        )

    )

    settings.export.filename = (

        st.sidebar.text_input(

            "Filename",

            settings.export.filename

        )

    )

    return settings