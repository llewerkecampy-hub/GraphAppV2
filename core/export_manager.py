# core/export_manager.py

import io

from PIL import Image

from core.models import (
    ExportSettings
)


# =====================================================
# Constants
# =====================================================

EXPORT_FORMATS = [

    "png",
    "svg",
    "pdf",
    "tiff"

]

SUPPORTED_DPI = [

    300,
    600,
    1200

]


# =====================================================
# Validation
# =====================================================

def validate_export_settings(
    settings
):

    if settings.file_format.lower() not in EXPORT_FORMATS:

        raise ValueError(
            f"Unsupported export format: "
            f"{settings.file_format}"
        )

    if settings.dpi not in SUPPORTED_DPI:

        raise ValueError(
            f"Unsupported DPI: "
            f"{settings.dpi}"
        )

    return True


# =====================================================
# Generic Save
# =====================================================

def save_matplotlib_figure(
    fig,
    destination,
    file_format,
    dpi,
    transparent
):

    fig.savefig(

        destination,

        format=file_format,

        dpi=dpi,

        bbox_inches="tight",

        transparent=transparent

    )


# =====================================================
# Standard Buffer
# =====================================================

def figure_to_buffer(
    fig,
    settings
):

    validate_export_settings(
        settings
    )

    buffer = io.BytesIO()

    save_matplotlib_figure(

        fig,

        buffer,

        settings.file_format,

        settings.dpi,

        settings.transparent

    )

    buffer.seek(0)

    return buffer


# =====================================================
# TIFF Buffer
# =====================================================

def tiff_buffer(
    fig,
    settings
):

    png_buffer = io.BytesIO()

    save_matplotlib_figure(

        fig,

        png_buffer,

        "png",

        settings.dpi,

        settings.transparent

    )

    png_buffer.seek(0)

    image = Image.open(
        png_buffer
    )

    output = io.BytesIO()

    image.save(

        output,

        format="TIFF",

        compression="tiff_lzw"

    )

    output.seek(0)

    return output


# =====================================================
# Download Buffer
# =====================================================

def get_download_buffer(
    fig,
    settings
):

    validate_export_settings(
        settings
    )

    if (

        settings.file_format.lower()

        ==

        "tiff"

    ):

        return tiff_buffer(
            fig,
            settings
        )

    return figure_to_buffer(
        fig,
        settings
    )


# =====================================================
# Save To Disk
# =====================================================

def export_figure(
    fig,
    settings
):

    validate_export_settings(
        settings
    )

    filepath = (

        f"{settings.filename}."

        f"{settings.file_format}"

    )

    if (

        settings.file_format.lower()

        ==

        "tiff"

    ):

        buffer = tiff_buffer(
            fig,
            settings
        )

        with open(
            filepath,
            "wb"
        ) as out:

            out.write(
                buffer.read()
            )

        return filepath

    save_matplotlib_figure(

        fig,

        filepath,

        settings.file_format,

        settings.dpi,

        settings.transparent

    )

    return filepath


# =====================================================
# MIME Types
# =====================================================

def get_mime_type(
    file_format
):

    file_format = (
        file_format.lower()
    )

    mime_types = {

        "png":
        "image/png",

        "svg":
        "image/svg+xml",

        "pdf":
        "application/pdf",

        "tiff":
        "image/tiff"

    }

    return mime_types.get(

        file_format,

        "application/octet-stream"

    )