
# About
This is a simple `.json` and `.txt` pack of files that have a list of 187.156 words in 42 languages, all words are in lowercase and contain no special characters nor numbers.
The **words have the same order** in all the files, so the word number 85623 in file `no.json` is the translation of the word 85623 in any other file, so every single word is the translation of it's parallel word in all the other files.

# Usage
You can just load the `.json` files since they are small and easy to parse, or you can use the `.txt`.

Here are some starter codes for loading the `.json` files:

```javascript
const fs = require('fs');
const words = JSON.parse(fs.readFileSync('en.json', 'utf8'));
```

```python
import json
with open('en.json', 'r', encoding="utf-8") as f:
    words = json.load(f)
```

```php
$words = json_decode(file_get_contents('en.json'), true);
```


# Languages
- `af.json` - Afrikaans
- `be.json` - Belarusian
- `bn.json` - Bengali
- `da.json` - Danish
- `el.json` - Greek
- `es.json` - Spanish
- `fr.json` - French
- `hi.json` - Hindi
- `id.json` - Indonesian
- `it.json` - Italian
- `ja.json` - Japanese
- `ko.json` - Korean
- `lv.json` - Latvian
- `nl.json` - Dutch
- `pl.json` - Polish
- `ru.json` - Russian
- `sl.json` - Slovenian
- `sv.json` - Swedish
- `tl.json` - Tagalog
- `uk.json` - Ukrainian
- `uz.json` - Uzbek
- `ar.json` - Arabic
- `bg.json` - Bulgarian
- `cn.json` - Chinese
- `de.json` - German
- `en.json` - English
- `fi.json` - Finnish
- `ga.json` - Irish
- `hr.json` - Croatian
- `is.json` - Icelandic
- `iw.json` - Hebrew
- `ka.json` - Georgian
- `lb.json` - Luxembourgish
- `mt.json` - Maltese
- `no.json` - Norwegian
- `pt.json` - Portuguese
- `ro.json` - Romanian
- `sk.json` - Slovak
- `sr.json` - Serbian
- `th.json` - Thai
- `ur.json` - Urdu
- `vi.json` - Vietnamese



# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

# Credits
This work was derived from the repository [english-words](https://github.com/dwyl/english-words) by [dwyl](https://github.com/dwyl)


