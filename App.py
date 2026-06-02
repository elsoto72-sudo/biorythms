from datetime import datetime, timedelta
import math
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(
    page_title="Βιορυθμοί με Διάγραμμα", page_icon="📈", layout="centered"
)

st.title("📈 Δυναμικοί Βιορυθμοί")
st.write(
    "Δείτε την πορεία του Φυσικού, Συναισθηματικού και Πνευματικού σας κύκλου για τις επόμενες 30 ημέρες."
)

# Εισαγωγή ημερομηνίας
birth_date = st.date_input(
    "Επιλέξτε την ημερομηνία γέννησής σας:",
    value=datetime(1990, 1, 1),
    min_value=datetime(1920, 1, 1),
    max_value=datetime.now(),
)

if st.button("Υπολογισμός & Σχεδίαση", type="primary"):
    current_date = datetime.now().date()

    # Δημιουργία δεδομένων για τις επόμενες 30 ημέρες
    dates = [current_date + timedelta(days=i) for i in range(30)]
    days_lived_today = (current_date - birth_date).days

    physical_values = []
    emotional_values = []
    intellectual_values = []
    formatted_dates = []

    for i in range(30):
        t = days_lived_today + i
        date_label = dates[i].strftime("%d/%m")
        formatted_dates.append(dates[i])

        # Υπολογισμός ημιτόνων
        p = math.sin(2 * math.pi * t / 23) * 100
        e = math.sin(2 * math.pi * t / 28) * 100
        i_val = math.sin(2 * math.pi * t / 33) * 100

        physical_values.append(p)
        emotional_values.append(e)
        intellectual_values.append(i_val)

    # Εμφάνιση των σημερινών τιμών σε Metrics
    st.subheader(f"🗓️ Σήμερα (Ημέρες Ζωής: {days_lived_today})")
    col1, col2, col3 = st.columns(3)
    col1.metric("Φυσικός (23η)", f"{round(physical_values[0], 1)}%")
    col2.metric("Συναισθηματικός (28η)", f"{round(emotional_values[0], 1)}%")
    col3.metric("Πνευματικός (33η)", f"{round(intellectual_values[0], 1)}%")

    st.write("---")
    st.subheader("📊 Πρόβλεψη Επόμενων 30 Ημερών")

    # Δημιουργία του Plotly Διαγράμματος
    fig = go.Figure()

    # Φυσικός Κύκλος (Κόκκινο)
    fig.add_trace(
        go.Scatter(
            x=formatted_dates,
            y=physical_values,
            mode="lines",
            name="Φυσικός (Σώμα)",
            line=dict(color="#ef553b", width=3),
        )
    )

    # Συναισθηματικός Κύκλος (Μπλε)
    fig.add_trace(
        go.Scatter(
            x=formatted_dates,
            y=emotional_values,
            mode="lines",
            name="Συναισθηματικός",
            line=dict(color="#636efa", width=3),
        )
    )

    # Πνευματικός Κύκλος (Πράσινο)
    fig.add_trace(
        go.Scatter(
            x=formatted_dates,
            y=intellectual_values,
            mode="lines",
            name="Πνευματικός (Διάνοια)",
            line=dict(color="#00cc96", width=3),
        )
    )

    # Οριζόντια γραμμή του μηδενός (Κρίσιμο σημείο)
    fig.add_shape(
        type="line",
        x0=formatted_dates[0],
        y0=0,
        x1=formatted_dates[-1],
        y1=0,
        line=dict(color="gray", width=1.5, dash="dash"),
    )

    # Ρυθμίσεις εμφάνισης διαγράμματος
    fig.update_layout(
        xaxis_title="Ημερομηνία",
        yaxis_title="Κατάσταση (%)",
        yaxis=dict(range=[-110, 110]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=20, b=20),
        hovermode="x unified",
    )

    # Εμφάνιση στην οθόνη
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "💡 **Πώς να το διαβάσεις:** Όταν μια γραμμή τέμνει την οριζόντια διακεκομμένη γραμμή (0%), η ημέρα εκείνη θεωρείται **κρίσιμη** για τον αντίστοιχο τομέα."
    )
