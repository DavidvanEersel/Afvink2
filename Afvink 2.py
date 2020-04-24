from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def submit():
    sequentie = request.args.get("Sequentie")
    if sequentie is not None:
        eiwit = calculate(sequentie.lower())
        return render_template("afvink2.html", eiwit="De eiwit sequentie is "+eiwit)
    return render_template("afvink2.html", sequentie=sequentie)


def calculate(seq):
    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
            'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
            'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
            'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
            'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
            'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
            'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
            'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
            'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
            'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
            'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
            'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
            'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
            'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
            'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
            'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}
    eiwit = ""
    startcodon = seq.find("atg")
    for i in range(startcodon, len(seq), 3):
        try:
            codon = seq[i:i + 3]
            if code[codon] == "*":
                eiwit += "* Einde eiwit sequentie"
                break
            eiwit += (code[codon])
        except KeyError:
            break
    return eiwit


if __name__ == '__main__':
    app.run()
