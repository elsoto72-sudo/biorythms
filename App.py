from datetime import datetime
import math
import streamlit as st

# Ρύθμιση σελίδας για κινητά
st.set_page_config(page_title="Βιορυθμοί", page_icon="📊", layout="centered")

st.title("📊 Υπολογισμός Βιορυθμών")
st.write("Μάθετε τη φάση του σώματος, του συναισθήματος και του πνεύματός σας σήμερα.")

# Εισαγωγή ημερομηνίας με εύχρηστο ημερολόγιο
birth_date = st.date_input(
    "Επιλέξτε την ημερομηνία γέννησής σας:",
    value=datetime(1990, 1, 1),
    min_value=datetime(1920, 1, 1),
    max_value=datetime.now(),
)

if st.button("Υπολογισμός", type="primary"):
    current_date = datetime.now().date()
    days_lived = (current_date - birth_date).days

    # Κύκλοι
    p = round(math.sin(2 * math.pi * days_lived / 23) * 100, 1)
    e = round(math.sin(2 * math.pi * days_lived / 28) * 100, 1)
    i = round(math.sin(2 * math.pi * days_lived / 33) * 100, 1)

    def get_status(v):
        if v > 50:
            return "🟢 Υψηλή Φάση (Ακμή)"
        if v < -50:
            return "🔴 Χαμηλή Φάση (Αποφόρτιση)"
        if -10 <= v <= 10:
            return "⚠️ Κρίσιμη Ημέρα (Μετάβαση)"
        return "🔵 Σταθερή / Μεταβατική"

    st.subheader(f"🗓️ Συνολικές ημέρες ζωής: {days_lived}")

    # Εμφάνιση αποτελεσμάτων με όμορφα κουτιά (Metrics)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Φυσικός (23η)", value=f"{p}%")
        st.caption(get_status(p))
    with col2:
        st.metric(label="Συναισθηματικός (28η)", value=f"{e}%")
        st.caption(get_status(e))
    with col3:
        st.metric(label="Πνευματικός (33η)", value=f"{i}%")
        st.caption(get_status(i))

    # Μια μικρή επεξήγηση στο τέλος
    st.info(
        "💡 **Σημείωση:** Οι κρίσιμες ημέρες (κοντά στο 0%) είναι μέρες μετάβασης όπου χρειάζεται περισσότερη προσοχή."
    )
