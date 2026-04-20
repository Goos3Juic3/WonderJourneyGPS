def generate_summary(town_name, pros, cons):
    pros_text = ", ".join(pros) if pros else "no major highlights"
    cons_text = ", ".join(cons) if cons else "no major downsides"

    return (
        f"Approaching {town_name}. "
        f"Pros include {pros_text}. "
        f"Cons include {cons_text}."
    )
