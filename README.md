# Word Map
This project is implemented for NLP Course and the subject is : Pop and Rap musics recognition.

## Data Collection
Lyrics were collected from [Radio Javan](www.radiojavan.com) with web crawler written in python. music's URL is given to the crawler and the music's lyrics is extracted to a .txt file.

Pop artists choosen : 
- Mohsen Yeganeh : 57 songs
- Babak Jahanbakhsh : 50 songs

Rap artists choosen : 
- Hichkas : 13 songs
- Bahram : 20 songs
- Amir Khalvat : 8 songs
- Ali Sorena : 10 songs
- Quf : 8 songs

## Processing the lyrics
Normalization and Tokenizing the lyrics is done by [hazm](http://www.sobhe.ir/hazm/) python module.
after normalizing and extracting the words, we store the words and how many times they were repeated in the lyrics in the artist's exclusive dictionary and category's dictionary (example : Mohsen Yeganeh words are stored in mohsenYDict and popDict)
by founding out the exact number of words repeatition, we can now have our word maps.


## Results
### Pop
The main message from pop songs is talking from love and they address their beloved and their heart and feelings and tell them about things that they could do but didn't and they express their regret. They talk about their wishes and what are they going to do for their beloved and their life and telling their beloved filled their minds always.

### Rap
Rappers try to convey their critical messages. They criticize the political and social situation and the lives of people Or emphasize on empowerment or self-improvement. They speak more of themselves or of collective movements in their poems and talk directly to their audience. The use of conditional sentences and the unavoidable aspirations and frustrations of other features of their poetry. Most of their messages contain negative sentences
