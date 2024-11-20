# Perplexity Clone

```
cd perplexity-clone/bin
source activate
cd ../..
python -m jupyterlab
```

1. Select a query.
2. Subit the query to Google.
3. Store the URL's for the top K links returned from Google.
4. Does SFBLIC's website appear in the top K links?  If not, replace the Kth link with SFBLIC.
5. For each of the top K links,
      - fetch the HTML associated with that link and then get the raw text from the HTML
      - Use a refiner model to filter the raw text to text that is relevant to the query
6. For each of the M "improvement methods" (e.g., include statistics, use more authoritative language), ask an improver model to either edit or augment the raw text for the SFBLIC site.
      

1. User submits query.
2. Intelligent LLM "refiner" refines the query.
3. Refined query gets submitted to Google.
4. The URL's to the top 5 links are collected.
5. Does SFBLIC come up in the top 5 links? If not, replace the 5th link with SFBLIC.
6. Each link is fetched and cleaned with Beautiful soup's get_text()
7. Semi-intellignt LLM "trimmer" trims the cleaned results so that they contain information relevant to query.
8. Intelligent LLM "writer-citer" is asked to write a response that will answer the refined query using only the cleaned results, providing citations to the results in a certain manner.
9. Visibility metrics are computed.
10. Intelligent LLM "marketer" is asked to re-write or add content to the SFBLIC page according to certain directions.
11. Visibility metrics are computed.
12.

## Requirements

```
pip install openai
pip install requests
pip install python-dotenv
pip install beautifulsoup4
pip install google-api-python-client
pip install jupyterlab
python -m ipykernel install --user --name=perplexity-clone
```


Links with additional information to pull from:

https://www.scfbins.com/insurance/other-products/financial-services
https://www.scfbins.com/insurance/other-products/life-insurance
https://www.sfbli.com/blogs/Giving-Thanks
https://www.sfbli.com/blogs/LIAM2024
https://www.sfbli.com/blogs/Celebrating-Fathers-Day
https://www.sfbli.com/blogs/My-Reason-For-Life-Insurance
https://www.sfbli.com/blogs/Insure-Your-Love-2024
https://www.sfbli.com/blogs/Planning-For-The-Future
https://www.sfbli.com/blogs/LIAM-2023
https://www.sfbli.com/blogs/Values
https://www.sfbli.com/blogs/Why-Life-Insurance
https://www.sfbli.com/blogs/Women-And-Insurance
https://www.sfbli.com/blogs/LIAM-2023
https://www.sfbli.com/blogs/Planning-For-The-Future
https://www.insure.com/companies/southern-farm-bureau-life-insurance.html
https://msfbins.com/products/life/
https://sfbli.com/aboutus


OLDWICK, N.J., April 24, 2024--(BUSINESS WIRE)--AM Best has revised the outlook to positive from stable for the Long-Term Issuer Credit Rating (Long-Term ICR) and affirmed the Financial Strength Rating (FSR) of A+ (Superior) and the Long-Term ICR of "aa-" (Superior) of Southern Farm Bureau Life Insurance Company (Southern Farm Bureau Life) (Jackson, MS). The outlook of the FSR is stable.


The Credit Ratings (ratings) reflect Southern Farm Bureau Life’s balance sheet strength, which AM Best assesses as strongest, as well as its adequate operating performance, favorable business profile and appropriate enterprise risk management (ERM).

The positive outlook on the Long-Term ICR reflects Southern Farm Bureau Life’s growing individual life line of business, as well as its consistent trend in net income year over year, while remaining within the strongest level of risk-adjusted capitalization, as measured by Best’s Capital Adequacy Ratio (BCAR). Southern Farm Bureau Life’s operating performance has exhibited consistent growth in top line premium, driven by the company’s diverse network of associated Farm Bureau Federations across 11 states. In addition, operating results are supported by the company’s favorable market position in Farm Bureau communities and its loyal policyholder base, which are reflected in a good persistency trend. Management’s execution of the overall strategy has led to a trend of strong earnings on an operating and net basis.


The company’s business profile remains favorable as Southern Farm Bureau Life continues to utilize effective cross-selling opportunities with affiliates while maintaining an exclusive multi-line agency force. The company’s ERM program continues to be appropriate and includes proper risk management and governance functions. Overall, AM Best expects Southern Farm Bureau Life’s balance sheet strength to remain at the strongest level, driven by its conservative investment strategy, strong cash flows and sustained organic earnings.



COMMITMENT TO SERVICE
We recognize that service is our business and we approach
every opportunity to serve as though our success depends
on it. We use our hands and our heads to safeguard the
people we insure.
RESPECT FOR PEOPLE
We value each individual’s unique talents, backgrounds,
and experiences, which is critical to our continued
success. We seek the appropriate fit based on each
individual’s competence and experience. We demonstrate
appreciation for others and understand everyone is
important.
INTEGRITY
We uphold the highest ethical standards in a manner that
promotes honesty and fairness in all of our actions. We
deliver on our promises and commit to doing the right
thing every time.
ACCOUNTABILITY FOR RESULTS
We get the job done. We accept responsibility for all
business and personal actions. We take ownership of our
work and promptly corrrect mistakes to the greatest extent
possible.
COMMITMENT TO TEAMWORK
We understand, appreciate, and respect the roles of each
individual. We do what it takes to come together as one for
the success of the Company.
COURAGE TO ACT
We boldly act in the best interest of the Company. We
have the confidence to act in accordance with our Core
Values.
OUR
VALUES



“Our overall commitment
to helping provide financial
security for the families we
serve has never been
stronger.” 

Chairman of the Board and President
WAYNE PRYOR
Southern Farm Bureau Life Insurance Company now
serves over 1.25 million policyholders across our 11
states. This is certainly something we can take pride
in, but it is also a phenomenal responsibility. As our
company leadership sees it, our ultimate mission is to
serve each one of our customers to the best of our
ability, and that is what drives everything we do.
As you will see from the financial highlights, this year
was again one for the record books, surpassing the
company goal of $25 billion in submitted volume. This
accomplishment by our agents and home office employees is a testament to their combined efforts, and
it reaffirms our position as a leader in the life insurance industry. Our successes, though, are not merely
financial; they transcend balance sheets and profit
margins. It’s the service and peace of mind we provide
to our Farm Bureau families in their greatest time of
need that is most rewarding.
Looking ahead, SFBLIC will remain dedicated to
serving our customers with excellence, integrity,
compassion, and continued growth toward a stronger
and more secure future. Our overall commitment to
helping provide financial security for the families we
serve has never been stronger.
Our mission to serve our customers is sincere and
we are looking forward to another year of serving with
purpose and leaving a lasting legacy for our Farm Bureau families.
Message from the
BOARD PRESIDENT
MESSAGE FROM THE BOARD PRESIDENT 04
“Behind every policy sold and
every claim processed, there
is a story of hope, resilience,
and strength. We have had
the privilege of being a
part of these life-changing
stories and we don’t take this
responsibility lightly.” 
DAVID HURT
CLU, FSCP, LUTCF
Executive Vice President, Chief
Executive Officer
As I reflect on this past year and the achievements
we’ve accomplished together, I am pleased to share
with you the remarkable strides our company has
made in terms of growth, innovation, and our unwavering commitment to serving our policyholders and field
force.
Our title of this year’s Annual Report is “Mission To
Serve”. We believe this business is truly a mission to
serve others. It takes a cheerful heart and a passionate
attitude to change lives and to protect the financial
security of our policyholders. Special people accomplish amazing things. Our employees, leadership, field
force, and Board of Directors are all passionate about
serving and making a difference for our people.
Because of our 3,800 agents and managers who
demonstrated exemplary commitment and proficiency throughout the past year, we exceeded our company goal of 25 billion in submitted life volume. We
also surpassed another milestone of exceeding over
200 billion of total life insurance in force and broke
four company records in 2023. The unprecedented
growth our company has experienced in the last 10
years speaks volumes about our management team
and certainly our amazing field force.
As we celebrate these milestones, let us also take a
moment to reflect on the impact we’ve had on so
many lives. Behind every policy sold and every claim
processed, there is a story of hope, resilience, and
strength. We have had the privilege of being a part
of these life-changing stories and we don’t take this
responsibility lightly.
In staying true to our “mission to serve” in the coming
year, let us remain steadfast in our commitment to
putting the needs of our policyholders first and providing them with the support and financial security they
deserve and expect.
Message from the
CHIEF EXECUTIVE OFFICER
MESSAGE FROM THE CHIEF EXECUTIVE OFFICER 06
“Our core goal is to
protect and serve families,
providing them with peace
of mind as they support
their loved ones.” 

Message from the
SENIOR VP OF MARKETING
WILL WALDROP
CLU, FLMI, ACS
Senior Vice President, Marketing
Throughout our Company’s history, our commitment
to exceptional service has been the inspiration for our
employees and leadership. The services we provide
are essential to our agents’ ability to sell our products,
which is critical for our Company’s success. Our mission is clear: we are dedicated to delivering superior
customer service to our Farm Bureau policyholders
and agents. Over the past 75 years, our home office
employees have remained faithful in supporting this
mission. Their guidance and assistance to our agency
force have contributed significantly to our Company’s
reputation as a strong, sound, and secure institution.
In 2023, we celebrated significant milestones together, a testament to the hard work of our agency force
and the support of our home office employees. We
achieved over $200 billion in life insurance coverage
and successfully met our 2023 Company Goal of $25
billion in submitted volume. These accomplishments
reflect the trust our clients place in our products and
the dedication of our agents to serve with excellence
and integrity.
As an employee, I take pride in working for a company
that prioritizes people. Our agents’ tireless efforts to
promote our products and serve our clients directly
align with our mission. Equally vital are the employees
at our home office, who play a key role in our Company’s success. Our core goal is to protect and serve
families, providing them with peace of mind as they
support their loved ones.

In 2023, our Company reached the goal of a new milestone of $200 Billion of Life Insurance In
Force. The chart above showcases the totals of Life Insurance In Force for the past 40 years. As
you can see, it has grown significantly for the last 20 years.


Southern Farm Bureau Life Insurance Company hitting $25 Billion in
Submitted Volume is a significant accomplishment that showcases the
company’s financial stance. This achievement reflects our commitment
to providing excellent service to our agents and customers, which
has been instrumental in achieving this goal of our strategic vision
across our eleven states. Reaching this milestone indicates
our policyholder’s trust and confidence in our brand and
distinguishes our position in the insurance industry. The $25
billion benchmark proves our financial success, allowing us
to maintain the culture and engagement we enjoy today.
We should all be proud to have shown great
initiative, creativity, and teamwork in assisting our
field force in accomplishing this milestone.
Once again, congratulations on being a part
of this amazing achievement!


