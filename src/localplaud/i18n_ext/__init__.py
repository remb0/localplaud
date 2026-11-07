"""Per-area translation catalogs merged into ``localplaud.i18n``.

Modules may export ``ZH_HANT_TW`` or ``NL`` dictionaries mapping English
source strings to Traditional Chinese for Taiwan or Dutch. Splitting catalogs by product
area keeps parallel UI work from colliding in one giant dictionary. Modules are
merged in name order; the core catalog in ``i18n.py`` wins on conflicts.
"""

from __future__ import annotations

import importlib
import pkgutil


def extra_catalog(locale: str) -> dict[str, str]:
    attribute = {"zh-Hant-TW": "ZH_HANT_TW", "nl": "NL"}.get(locale)
    if attribute is None:
        return {}
    merged: dict[str, str] = {}
    for module_info in sorted(pkgutil.iter_modules(__path__), key=lambda item: item.name):
        module = importlib.import_module(f"{__name__}.{module_info.name}")
        merged.update(getattr(module, attribute, {}) or {})
    return merged
