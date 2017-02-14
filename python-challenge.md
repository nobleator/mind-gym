# http://www.pythonchallenge.com/

## Level 1
Replace `0.html` in the URL bar with `274877906944.html` (the value of 2^38).

## Level 2
`def level1(text):
  result = ""
  ctr = 0
  while ctr < len(text):
    if text[ctr] in ascii_lowercase:
      indx = ascii_lowercase.index(text[ctr])
      if indx > len(ascii_lowercase) - 1:
        result += ascii_lowercase[indx + 2]
      else:
        result += ascii_lowercase[indx - 24]
    else:
      result += text[ctr]
    ctr += 1
  return result`
 
Call the above function on the string:
"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
This returns the string:
"i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
Call the function on the string "map", then replace `map.html` with the output of the function, `ocr.html`.
