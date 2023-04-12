import openai

openai.api_key = "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"

prompt = """Decide whether a journal entry's sentiment is positive, neutral, or negative and summarize it in 1-2 sentences.

Journal entry: Mich beschäftig schon seit Tagen das gleiche Thema. Ich bekomme immer das Gefühl mir selbst weniger Vertrauen zu können. Ich bin ängstlich im Bezug auf viele Dinge. Allen voran all das was mit Alex zu tun hat. Als wie wenn ich es ihr nicht zutrauen würde, dass sie all die Situationen schaffen würde. Aber das tut sie. Sie ist stark und gerade im Wachstumsprozess. Also darf ich auch auf ihre Fähigkeiten vertrauen. Doch woher kommt diese Angst? Es fühlt sich an wie ein leichtes Trauma. Angefangen durch den Bad Trip von ihr, verstärkt durch den Tod von Mama. Seitdem gehe ich anders und nicht mehr so sorgenfrei ins Leben. Was dem ganzen natürlich auch nicht hilft ist das ständige kiffen im Moment. Auch wenn es nur die letzten 1-2 Wochen war. Trotzdem sollte ich mich fragen wo mich das hinführt. Will ich das? Wo will ich generell hin? Ich will wieder produktiv sein, jeden Tag das Gefühl haben wirklich etwas geschafft zu haben. Und nicht nur das, sondern harte Arbeit. Ich will dieses Leben wo ich dauerhaft unter Strom stehe und meine 12 Stunden arbeite. Warum? Weil dort Erfolg und das größte Wachstum liegt. Man kommt nicht weit mit einem gemütlichen Leben. Auch wenn sich nicht das ganze Leben um arbeiten drehen sollte liegt das Geheimnis und die Freude doch in den aufgewendeten Stunden und dem Output. Das gibt mir das Gefühl ich kann mir selbst wieder mehr Vertrauen. Mehr Selbstsicherheit. Denn wenn ich diese Dinge schaffe wenn ich sie mir vornehme, kann ich mir Vertrauen auch andere Dinge zu schaffen.!
Sentiment:"""

response = openai.Completion.create(engine="text-davinci-003",  prompt=prompt, max_tokens=60)

print(response)



# python install
# install openai package
# embeddings and analysis


# read journal from .txt file

# define in prompt that GPT should act as therapist with the goal of helping people and find their bad patterns and things they should not ignore
