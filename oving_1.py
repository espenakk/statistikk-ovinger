import statistics, pandas as pd

#Oppgave 1
poengsum = [2, 8, 10, 7, 10, 5, 2, 8, 2, 10]

gjennomsnitt = sum(poengsum) / len(poengsum)
median = statistics.median(poengsum)

print("Gjennomsnitt:", gjennomsnitt)
print("Median:", median)

#Oppgave 2
data = {
    "Student": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Antall timer": [5, 7, 6, 6, 6, 5, 6, 1, 5, 5]
}

df = pd.DataFrame(data)
print(df)

antall_timer = data["Antall timer"]

mean = statistics.mean(antall_timer)
median = statistics.median(antall_timer)
stdev = statistics.stdev(antall_timer)

print(f"Gjennomsnitt: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {stdev}")

#Oppgave 3
karakter_data = {
    "Karakter": [1, 2, 3, 4, 5, 6],
    "Antall": [2, 5, 5, 2, 6, 3]
}

karakter_df = pd.DataFrame(karakter_data)
print(karakter_df)

karakter = karakter_data["Karakter"]
antall = karakter_data["Antall"]

weighted_sum = sum(k * a for k, a in zip(karakter, antall))
total_count = sum(antall)
mean_karakter = weighted_sum / total_count

print(f"Gjennomsnittskarakter: {mean_karakter}")

#Oppgave 4
konsentrasjon_data = {
    "Kolbe nr.": [1, 2, 3, 4, 5, 6, 7, 8],
    "Konsentrasjon NaOH": [0.1109, 0.0951, 0.0862, 0.1015, 0.1579, 0.0981, 0.0925, 0.0987]
}

konsentrasjon_df = pd.DataFrame(konsentrasjon_data)

# Remove the outlier (Kolbe nr 5)
konsentrasjon_df = konsentrasjon_df[konsentrasjon_df["Kolbe nr."] != 5]
print(konsentrasjon_df)

konsentrasjon_naoh = konsentrasjon_df["Konsentrasjon NaOH"]

mean_konsentrasjon = statistics.mean(konsentrasjon_naoh)
median_konsentrasjon = statistics.median(konsentrasjon_naoh)
stdev_konsentrasjon = statistics.stdev(konsentrasjon_naoh)

print(f"Gjennomsnitt Konsentrasjon NaOH: {mean_konsentrasjon}")
print(f"Median Konsentrasjon NaOH: {median_konsentrasjon}")
print(f"Standard Deviation Konsentrasjon NaOH: {stdev_konsentrasjon}")

dataset = [0.38, 0.39, 0.25, 0.89, 0.48, 0.59]
mean = statistics.mean(dataset)
variance = statistics.variance(dataset)
print(f"Sample Variance: {variance}")
print(f"Mean: {mean}")