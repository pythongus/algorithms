from algo.one_time_pad import decrypt


if __name__ == "__main__":
    text = ("""v+6aq2LWK6j=~/J,Nl$<]DsvAiM1L*6FOlwQ:=tR}y;lhI]2$#uVd\\"""
            """#JXkIF4\\(*NR8OrOaHt 3oO0;DL]\'I3^?``X\\X!QIGy6\'/892?o"""
            """1p9cgfUn#u(u@YQ> )WXq+dNIRdbt9?\\^{X0="F*u""")
    key = """<place key here>"""
    print(decrypt(text, key))
