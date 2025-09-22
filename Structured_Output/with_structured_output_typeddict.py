from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model = ChatOpenAI()


"""
#schema
class Review(TypedDict):
    summary: Annotated[str,"A brief summary of the review."]
    sentiment: Annotated[str,"Return sentiment of the review either negative positive or neutral"]
    
structured_model = model.with_structured_output(Review)


result = structured_model.invoke("The hardware is great, but software feels bloated.
                        There are too many pre-installed apps that I can't remove.
                        Also, the UI looks outdated compared to other brands.
                        Hoping for a software update to fix this.")

print('Overall Result:',result)
print('Summary:',result['summary'])
print('Sentiment:',result['sentiment'])
"""

class Review(TypedDict):
    key_themes: Annotated[ list[str],'Write down all the key themes discussed in the review in a list']
    summary: Annotated[str,'A brief summary of review.']
    sentiment: Annotated[Literal["Postive","Negative"],"Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    name: Annotated[str,'Write the name of Reviewer']
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Ashish
""")

print('Overall Result:',result),
print('Pros:',result['pros']),
print('Cons:',result['cons']),
print('Summary:',result['summary'])
print('Sentiment:',result['sentiment'])
print('Reviewer Name:', result['name'])

# Problem no gurantee from LLM of return type will be string or int. No data validation is done. 
# Solution is Pydantic

 