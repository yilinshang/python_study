text = "X-DSPAM-Confidence:    0.8475"
zeropos = text.find('0')
num = text[zeropos:]
num = float(num)
print num