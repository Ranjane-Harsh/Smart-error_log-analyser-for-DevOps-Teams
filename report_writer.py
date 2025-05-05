def write_txt_report(filepath, clusters):
    with open(filepath,"w") as file:
        for grp_num,(fingerprint,cleaned_lines) in enumerate(clusters.items(), start=1):
            file.write(f"Group Number :{grp_num}\n")
            formatted = ",".join(fingerprint)
            file.write(f"Fingerprint : {formatted}\n")
            file.write(f"Few examples for the fingerprint :\n ")
            for idx,line in enumerate(cleaned_lines[:2], start=1):
                file.write(f"{idx}.{line}\n")
            file.write("-"*40+"\n")
