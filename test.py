# from __future__ import print_function
from textstat.textstat import textstat

if __name__ == '__main__':

        test_data1 = """Far up in the mountains of Canada, there is an old abandoned log cabin. Once it was occupied by a young couple who wanted to distance themselves from the chaos of this modern world. Here they were miles away from the nearest town. Bob, the husband, made the occasional trip into town to buy supplies whereas Jan, his wife, spent her free time by the fire, sewing. Their life was simply idyllic.
Then, one midwinter's day, Jan woke up from bed with a strange ache in her bones. Putting it down to overwork, Bob shooed her to bed and made sure she rested. Though Jan was impatient to get to her chores, Bob soothed her, "Relax, Sugar. You're overdoing things. All these chores will be here when you recover."

However, Jan seemed to be getting worse instead of recovering. By evening, she was running a high fever and in greater pain. In spite of his best efforts, Bob could not manage to ease her suffering. And then suddenly, she started to lapse into unconsciousness.

It was then obvious that she was seriously ill. What could Bob do? He had no experience in treating the sick and Jan was getting worse by the minute. He knew that there was an old doctor in town but he lived three miles away, downhill. Pot-bellied and obese, there was no way the doctor could make it up to their cabin.

Something had to be done quickly! Bob racked his brains but to no avail. The only thing left to do was to go to the doctor. In Jan's condition, she could never walk that far in the waist-deep snow. Bob would have to carry her!

Bob searched his mind for a way to move poor, sick Jan. Then, he remembered. He had once made a sledge so that they could ride together over the mountain. They never got around to using it though, because the whole mountain was thickly covered with rocks and trees. He had never found a safe way down, not even once.

"Well," he thought, "looks like I'm going to have to try it anyhow," as he dug out the sledge from the storeroom. "Jan may die unless I get her to the doctor, and life means nothing to me without her." With this thought in mind, Bob gently tucked Jan into the sledge, got in the front, and with a short prayer for safety, pushed off.

How they got through that ride alive, Bob has never figured out. As trees loomed up in front of him and just as quickly whizzed by his side, close enough to touch, he felt relieved that Jan was not awake to experience the ride. It was all he could do not to scream as collision seemed imminent, time and again, with only inches to spare.

At last, bursting from the mountainside, the town came into view. Barely slowing down, they sped through the icy streets, only losing speed as they neared the doctor's house. The sledge, battered through the journey, collapsed in the left ski as it came to a halt, spilling out its occupants. Bob picked up his Jan and made his way into the doctor's house.

After what seemed to be a long winter, Jan recovered fully from her illness but Bob never recovered from his fright. They moved into the little town so as to be near help in times of crisis, and have lived there ever since"""

        test_data = """Playing ... games has always been thought to be important to the development of well-balanced and creative children; however, what part, if any, they should play in the lives of adults has never been researched that deeply. I believe that playing games is every bit as important for adults as for children. Not only is taking time out to play games with our children and other adults valuable to building interpersonal relationships but is also a wonderful way to release built up tension.

There's nothing my husband enjoys more after a hard day of work than to come home and play a game of Chess with someone. This enables him to unwind from the day's activities and to discuss the highs and lows of the day in a non-threatening, kick back environment. One of my most memorable wedding gifts, a Backgammon set, was received by a close friend. I asked him why in the world he had given us such a gift. He replied that he felt that an important aspect of marriage was for a couple to never quit playing games together. Over the years, as I have come to purchase and play, with other couples & coworkers, many games like: Monopoly, Chutes & Ladders, Mastermind, Dweebs, Geeks, & Weirdos, etc. I can reflect on the integral part they have played in our weekends and our "shut-off the T.V. and do something more stimulating" weeks. They have enriched my life and made it more interesting. Sadly, many adults forget that games even exist and have put them away in the cupboards, forgotten until the grandchildren come over.

All too often, adults get so caught up in working to pay the bills and keeping up with the "Joneses'" that they neglect to harness the fun in life; the fun that can be the reward of enjoying a relaxing game with another person. It has been said that "man is that he might have joy" but all too often we skate through life without much of it. Playing games allows us to: relax, learn something new and stimulating, interact with people on a different more comfortable level, and to enjoy non-threatening competition. For these reasons, adults should place a higher priority on playing games in their lives"""
        

        test_data2 = """Where the amount of the annuity derived by the taxpayer during a year of income is more than, or less than, the amount payable for a whole year, the amount to be exclude from the amount so derived is the amount which bears to the amount which, but for this sub-section, would be the amount to be so, excluded the same proportion as the amount so derived bears to the amount payable for the whole year."""
        test_data3 = """I went to sleep with gum in my mouth and now there's gum in my hair and when I got out of bed this morning I tripped on my skateboard and by mistake I dropped my sweater in the sink while the water was running and I could tell it was going to be a terrible, horrible, no good, very bad day. I think I'll move to Australia."""

        TS = textstat


        
        print("flesch_reading_ease")
        print(TS.flesch_reading_ease(test_data))
        print("SMOG")
        print(TS.smog_index(test_data))
        print("flesch_kincaid_grade")
        print(TS.flesch_kincaid_grade(test_data))
        print("Coleman_Liau_Index")
        print(TS.coleman_liau_index(test_data))
        print("Automated_Readability_Index")
        print(TS.automated_readability_index(test_data))
        print("Dale_Chall_Readability_Score")
        print(TS.dale_chall_readability_score(test_data))
        print("difficult_words")
        print(TS.difficult_words(test_data))
        print("Linsear_Write_Formula")
        print(TS.linsear_write_formula(test_data))
        print( "gunning_fog")
        print(TS.gunning_fog(test_data))
        print("text_standard")
        print(TS.text_standard(test_data))
