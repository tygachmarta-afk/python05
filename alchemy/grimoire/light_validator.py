def validate_ingredients(ingredients: str) -> str:
    # Late import: the spellbook is only needed when this function runs,
    # not while the module is loading, so the import cycle never forms.
    from .light_spellbook import light_spell_allowed_ingredients

    lowered = ingredients.lower()
    for allowed in light_spell_allowed_ingredients():
        if allowed in lowered:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"