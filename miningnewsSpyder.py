
import sd_algorithm     #sd algoithm loaded from the file above
import pandas as pd

# dataframe to convert to csv and use  
df = pd.DataFrame()

#The newspapers used for mining

#1. CBS
#2. BBC
#3. The guardian
#4. Aljazeera

# Function to get news content from url
def website_content(url):
    sd.url = url
    content = sd.analyze_page()
    return content


# all links to mine data for all the categories
all_links = [
             'https://www.cbsnews.com/news/gottlieb-covid-infections-hot-spots-face-the-nation/',
             'https://www.cbsnews.com/news/evangelical-church-covid-19-pandemic-vaccine-skeptics/',
             'https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/',
             'https://www.cbsnews.com/news/capitol-riot-arrests-2021-04-02/',
             'https://www.cbsnews.com/news/william-evans-capitol-police-office-killed-lie-honor-rotunda/',
             'https://www.cbsnews.com/news/pelosi-matt-gaetz-removed-frobm-judiciary-committee-if-allegations-true/',
             'https://www.cbsnews.com/news/pet-adoption-surge-puppy-nannies-demand/',
             'https://www.cbsnews.com/news/supreme-court-sides-google-oracle-copyright-case/',
             'https://www.cbsnews.com/news/stimulus-check-veterans-waiting-payment/',
             'https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/',
             'https://www.cbsnews.com/news/facebook-hack-500-million-accounts/',
             'https://www.cbsnews.com/news/corporate-tax-global-minimum-rate-yellen/',
             'https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/',
             'https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/',
             'https://www.cbssports.com/golf/news/2021-masters-odds-favorites-why-you-should-root-for-these-nine-golfers-to-win-at-augusta-national/',
             'https://www.cbssports.com/wwe/news/wwe-raw-results-recap-grades-drew-mcintyre-bobby-lashley-stand-tall-ahead-of-wrestlemania-clash/live/',
             'https://www.cbssports.com/fantasy/baseball/news/fantasy-baseball-injury-reaction-fernando-tatis-likely-out-a-while-with-shoulder-subluxation-what-now/',
             'https://www.cbssports.com/college-basketball/news/2021-ncaa-tournament-bracket-college-basketball-scores-championship-game-schedule-stream-march-madness/',
             'https://www.cbsnews.com/news/dmx-hospital-vigil-family/',
             'https://www.cbsnews.com/news/music-and-the-medici/',
             'https://www.cbsnews.com/news/carrie-underwood-album-of-gospel-standards-my-savior/',
             'https://www.cbsnews.com/news/dmx-heart-attack-hospitalized/',
             'https://www.cbsnews.com/news/stanford-womens-ncaa-tournament-chamnpions-2021-arizona/',
             'https://www.cbsnews.com/news/bridgerton-star-rege-jean-page-duke-of-hastings-season-2/',
             'https://www.bbc.com/news/uk-56645208','https://www.bbc.com/news/56129210','https://www.bbc.com/news/av/uk-politics-56646912',
             'https://www.bbc.com/news/uk-politics-56647573','https://www.bbc.com/news/uk-northern-ireland-56644797','https://www.bbc.com/news/uk-wales-56611091',
             'https://www.bbc.com/news/business-56644058','https://www.bbc.com/news/technology-56639088','https://www.bbc.com/news/business-56650685',
             'https://www.bbc.com/news/business-56646761','https://www.bbc.com/news/business-52567567','https://www.bbc.com/news/business-54454990',
             'https://www.bbc.com/sport/tennis/56649098','https://www.bbc.com/sport/tennis/56618948','https://www.bbc.com/sport/rugby-union/56650185',
             'https://www.bbc.com/sport/football/56001747','https://www.bbc.com/sport/athletics/54964728','https://www.bbc.com/sport/athletics/51800436',
             'https://www.bbc.com/culture/article/20191106-why-chinese-rappers-dont-fight-the-power','https://www.bbc.com/culture/article/20200218-the-best-james-bond-themes-that-never-made-it-to-the-screen',
             'https://www.bbc.com/culture/article/20191007-the-greatest-hip-hop-songs-of-all-time','https://www.bbc.com/culture/article/20210329-remembering-miss-fury-the-worlds-first-great-superheroine',
             'https://www.bbc.com/culture/article/20210305-caterina-van-hemessen-an-unknown-visual-pioneer','https://www.bbc.com/culture/article/20210326-how-african-fashion-has-conquered-film','https://www.aljazeera.com/news/2021/4/4/profile-who-is-jordans-prince-hamza',
             'https://www.aljazeera.com/news/2021/4/6/israels-president-to-announce-candidate-to-form-new-government',
             'https://www.aljazeera.com/news/2021/4/4/republican-senator-urges-scaled-down-us-infrastructure-plan',
             'https://www.aljazeera.com/news/2021/4/2/fears-of-low-turnout-as-bulgaria-prepares-to-vote-in-pandemic',
             'https://www.aljazeera.com/news/2021/4/5/putin-signs-law-allowing-him-two-more-terms-as-russias-leader',
             'https://www.aljazeera.com/news/2021/4/6/russia-ups-security-at-navalny-prison-ahead-of-planned-protest',
             'https://www.aljazeera.com/news/2021/4/6/lebanons-baalbek-reborn-temples-a-newly-launched-virtual-tour',
             'https://www.aljazeera.com/economy/2021/4/6/jal-to-retire-fleet-of-planes-that-use-pratt-whitney-engines',
             'https://www.aljazeera.com/economy/2021/4/5/race-to-the-bottom-yellen-makes-case-for-global-minimum-tax-rate',
             'https://www.aljazeera.com/economy/2021/4/5/gamestop-plans-1bn-share-sale-after-reddit-fuelled-rally',
             'https://www.aljazeera.com/economy/2021/4/5/global-stocks-rise-spurred-by-surge-in-us-employment-data',
             'https://www.aljazeera.com/economy/2021/4/5/dow-hits-new-record-as-brightening-outlook-unleashes-bulls',
             'https://www.aljazeera.com/sports/2021/3/28/pakistan-football-federation-office-attacked',
             'https://www.aljazeera.com/news/2021/3/27/indian-cricket-legend-tendulkar-tests-positive-for-coronavirus',
             'https://www.aljazeera.com/news/2021/3/26/football-star-thierry-henry-quitting-social-media-over-racism',
             'https://www.aljazeera.com/sports/2021/4/4/football-valencia-briefly-walk-off-pitch-after-alleged-racism',
             'https://www.aljazeera.com/news/2021/3/20/ncaa-slammed-for-inequality-between-mens-and-womens-facilities',
             'https://www.aljazeera.com/sports/2021/3/31/african-tribe-long-marginalised-in-india-seeks-sporting-glory',
             'https://www.aljazeera.com/economy/2021/4/2/us-court-orders-halt-to-satan-shoe-sales-in-nike-trademark-row',
             'https://www.aljazeera.com/economy/2021/3/19/the-fed-women-entrepreneurs-and-the-kardashians-long-goodbye',
             'https://www.aljazeera.com/news/2021/3/17/disneyland-to-reopen',
             'https://www.aljazeera.com/news/2021/3/15/beyonce-taylor-swift-make-history-as-women-dominate-grammys',
             'https://www.aljazeera.com/economy/2021/3/2/new-harry-potter-video-game-will-allow-trans-characters',
             'https://www.aljazeera.com/economy/2021/2/2/gamestop-stock-fizzles-80-from-last-weeks-spectacular-highs',
             'https://www.theguardian.com/politics/2021/apr/06/keir-starmer-apologises-for-visiting-jesus-church-behind-which-performed-gay-exorcisms',
             'https://www.theguardian.com/environment/2021/apr/06/co2-from-englands-road-plan-up-to-100-times-more-than-dft-says',
             'https://www.theguardian.com/society/2021/apr/06/uk-long-covid-patients-facing-postcode-lottery-for-support',
             'https://www.theguardian.com/uk-news/2021/apr/05/conservative-mp-cheryl-gillan-dies-after-long-illness',
             'https://www.theguardian.com/politics/2021/apr/05/mayor-of-london-sadiq-khan-cannabis-legalisation-drugs-commission',
             'https://www.theguardian.com/world/2021/mar/30/who-criticises-chinas-data-sharing-as-it-releases-covid-origins-report',
             'https://www.theguardian.com/business/2021/apr/06/retail-entrepreneur-philip-day-backs-deal-to-keep-peacocks-afloat',
             'https://www.theguardian.com/travel/2021/apr/05/travel-industry-frustrated-by-lack-of-clarity-on-road-map-to-reopening',
             'https://www.theguardian.com/commentisfree/2021/mar/30/biden-tariffs-brexit-britain-eu-big-tech',
             'https://www.theguardian.com/business/2021/apr/06/uk-electric-car-sales-covid-lockdown',
             'https://www.theguardian.com/uk-news/2021/apr/05/how-a-food-bank-is-helping-city-service-workers-survive-the-pandemic',
             'https://www.theguardian.com/money/2021/mar/29/britons-pay-back-most-on-debt-in-27-years-as-credit-card-spending-slumps-covid',
             'https://www.theguardian.com/football/2021/apr/06/lille-win-psg-a-reminder-fame-ligue-1-france-title-race',
             'https://www.theguardian.com/football/2021/apr/05/wolves-west-ham-premier-league-match-report',
             'https://www.theguardian.com/football/2021/apr/05/ousmane-dembele-barcelona-real-valladolid-la-liga-el-clasico',
             'https://www.theguardian.com/football/2021/apr/05/championship-middlesbrough-watford-swansea-preston-roundup',
             'https://www.theguardian.com/football/football-league-blog/2021/apr/06/how-did-gillingham-become-the-only-efl-club-not-to-pay-agents-a-penny-football',
             'https://www.theguardian.com/sport/2021/mar/24/british-masters-golf-bid-for-crowds-at-proposed-covid-pilot-event-in-may',
             'https://www.theguardian.com/tv-and-radio/2021/apr/06/ainsley-harriott-i-talk-to-my-ingredients-when-im-cooking',
             'https://www.theguardian.com/lifeandstyle/2021/apr/05/how-we-met-i-was-terrified-my-parents-would-find-out-id-been-intimate-with-another-girl',
             'https://www.theguardian.com/film/2021/apr/06/terminator-rocky-godzilla-king-kong-versus-movie',
             'https://www.theguardian.com/media/2021/apr/06/brilliant-and-versatile-observer-and-guardian-journalist-sarah-hughes-dies-at-48',
             'https://www.theguardian.com/film/2021/apr/05/hear-me-out-why-serenity-isnt-a-bad-movie',
             'https://www.theguardian.com/food/2021/apr/06/barbecues-are-back-ten-perfect-burgers-to-try-from-vegan-bean-to-bhaji-bites'
]

article_content = []          #all the links content will be saved here
category = ['politics', 'business','sports', 'entertainment']       #all the category as mined following this order
content_category = [] 

# to create a link with categories equal to the links 
track = 0
change_cat = 0


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# There is a big big problem in the loop on the side of category. The loop misbehaves after the first iteration.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#every 6 iteration we change the category of the news we are mining
for link in all_links:
  sd = sd_algorithm.SDAlgorithm()
  content = website_content(link)
  article_content.append(content)
  content_category.append(category[change_cat])

  track += 1
  if track == 6:
    track = 0
    change_cat += 1 
    if change_cat == 4:
      change_cat = 0
    
df['content'] = article_content
df['content_category'] = content_category
df['link'] = all_links




# """ Getting contents from CBS News """

# # Political news
# sd = sd_algorithm.SDAlgorithm()
# cbsPol1 = get_content('https://www.cbsnews.com/news/gottlieb-covid-infections-hot-spots-face-the-nation/')
# sd = sd_algorithm.SDAlgorithm()
# cbsPol2 = get_content('https://www.cbsnews.com/news/evangelical-church-covid-19-pandemic-vaccine-skeptics/')
# sd = sd_algorithm.SDAlgorithm()
# cbsPol3 = get_content('https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/')
# sd = sd_algorithm.SDAlgorithm()
# cbsPol4 = get_content('https://www.cbsnews.com/news/capitol-riot-arrests-2021-04-02/')
# sd = sd_algorithm.SDAlgorithm()
# cbsPol5 = get_content('https://www.cbsnews.com/news/william-evans-capitol-police-office-killed-lie-honor-rotunda/')
# sd = sd_algorithm.SDAlgorithm()
# cbsPol6 = get_content('https://www.cbsnews.com/news/pelosi-matt-gaetz-removed-frobm-judiciary-committee-if-allegations-true/')

# # Business news
# sd = sd_algorithm.SDAlgorithm()
# cbsBus1 = get_content('https://www.cbsnews.com/news/pet-adoption-surge-puppy-nannies-demand/')
# sd = sd_algorithm.SDAlgorithm()
# cbsBus2 = get_content('https://www.cbsnews.com/news/supreme-court-sides-google-oracle-copyright-case/')
# sd = sd_algorithm.SDAlgorithm()
# cbsBus3 = get_content('https://www.cbsnews.com/news/stimulus-check-veterans-waiting-payment/')
# sd = sd_algorithm.SDAlgorithm()
# cbsBus4 = get_content('https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/')
# sd = sd_algorithm.SDAlgorithm()
# cbsBus5 = get_content('https://www.cbsnews.com/news/facebook-hack-500-million-accounts/')
# sd = sd_algorithm.SDAlgorithm()
# cbsBus6 = get_content('https://www.cbsnews.com/news/corporate-tax-global-minimum-rate-yellen/')

# # Sport news
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo1 = get_content('https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/')
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo2 = get_content('https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/')
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo3 = get_content('https://www.cbssports.com/golf/news/2021-masters-odds-favorites-why-you-should-root-for-these-nine-golfers-to-win-at-augusta-national/')
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo4 = get_content('https://www.cbssports.com/wwe/news/wwe-raw-results-recap-grades-drew-mcintyre-bobby-lashley-stand-tall-ahead-of-wrestlemania-clash/live/')
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo5 = get_content('https://www.cbssports.com/fantasy/baseball/news/fantasy-baseball-injury-reaction-fernando-tatis-likely-out-a-while-with-shoulder-subluxation-what-now/')
# sd = sd_algorithm.SDAlgorithm()
# cbsSpo6 = get_content('https://www.cbssports.com/college-basketball/news/2021-ncaa-tournament-bracket-college-basketball-scores-championship-game-schedule-stream-march-madness/')

# # Entertainment
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt1 = get_content('https://www.cbsnews.com/news/dmx-hospital-vigil-family/')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt2 = get_content('https://www.cbsnews.com/news/music-and-the-medici/')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt3 = get_content('https://www.cbsnews.com/news/carrie-underwood-album-of-gospel-standards-my-savior/')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt4 = get_content('https://www.cbsnews.com/news/dmx-heart-attack-hospitalized/')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt5 = get_content('https://www.cbsnews.com/news/stanford-womens-ncaa-tournament-chamnpions-2021-arizona/')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt6 = get_content('https://www.cbsnews.com/news/bridgerton-star-rege-jean-page-duke-of-hastings-season-2/')


# """ Getting contents from BBC """

# # Political news
# sd = sd_algorithm.SDAlgorithm()
# bbcPol1 = get_content('https://www.bbc.com/news/uk-56645208')
# sd = sd_algorithm.SDAlgorithm()
# bbcPol2 = get_content('https://www.bbc.com/news/56129210')
# sd = sd_algorithm.SDAlgorithm()
# bbcPol3 = get_content('https://www.bbc.com/news/av/uk-politics-56646912')
# sd = sd_algorithm.SDAlgorithm()
# bbcPol4 = get_content('https://www.bbc.com/news/uk-politics-56647573')
# sd = sd_algorithm.SDAlgorithm()
# bbcPol5 = get_content('https://www.bbc.com/news/uk-northern-ireland-56644797')
# sd = sd_algorithm.SDAlgorithm()
# bbcPol6 = get_content('https://www.bbc.com/news/uk-wales-56611091')

# # Business news
# sd = sd_algorithm.SDAlgorithm()
# bbcBus1 = get_content('https://www.bbc.com/news/business-56644058')
# sd = sd_algorithm.SDAlgorithm()
# bbcBus2 = get_content('https://www.bbc.com/news/technology-56639088')
# sd = sd_algorithm.SDAlgorithm()
# bbcBus3 = get_content('https://www.bbc.com/news/business-56650685')
# sd = sd_algorithm.SDAlgorithm()
# bbcBus4 = get_content('https://www.bbc.com/news/business-56646761')
# sd = sd_algorithm.SDAlgorithm()
# bbcBus5 = get_content('https://www.bbc.com/news/business-52567567')
# sd = sd_algorithm.SDAlgorithm()
# bbcBus6 = get_content('https://www.bbc.com/news/business-54454990')

# # Sport news
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo1 = get_content('https://www.bbc.com/sport/tennis/56649098')
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo2 = get_content('https://www.bbc.com/sport/tennis/56618948')
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo3 = get_content('https://www.bbc.com/sport/rugby-union/56650185')
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo4 = get_content('https://www.bbc.com/sport/football/56001747')
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo5 = get_content('https://www.bbc.com/sport/athletics/54964728')
# sd = sd_algorithm.SDAlgorithm()
# bbcSpo6 = get_content('https://www.bbc.com/sport/athletics/51800436')

# # Entertainment
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt1 = get_content('https://www.bbc.com/culture/article/20191106-why-chinese-rappers-dont-fight-the-power')
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt2 = get_content('https://www.bbc.com/culture/article/20200218-the-best-james-bond-themes-that-never-made-it-to-the-screen')
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt3 = get_content('https://www.bbc.com/culture/article/20191007-the-greatest-hip-hop-songs-of-all-time')
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt4 = get_content('https://www.bbc.com/culture/article/20210329-remembering-miss-fury-the-worlds-first-great-superheroine')
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt5 = get_content('https://www.bbc.com/culture/article/20210305-caterina-van-hemessen-an-unknown-visual-pioneer')
# sd = sd_algorithm.SDAlgorithm()
# bbcEnt6 = get_content('https://www.bbc.com/culture/article/20210326-how-african-fashion-has-conquered-film')


# """ Getting contents from The Aljazeera """

# # Political news
# sd = sd_algorithm.SDAlgorithm()
# newPol1 = get_content('https://www.aljazeera.com/news/2021/4/4/profile-who-is-jordans-prince-hamza')
# sd = sd_algorithm.SDAlgorithm()
# newPol2 = get_content('https://www.aljazeera.com/news/2021/4/6/israels-president-to-announce-candidate-to-form-new-government')
# sd = sd_algorithm.SDAlgorithm()
# newPol3 = get_content('https://www.aljazeera.com/news/2021/4/4/republican-senator-urges-scaled-down-us-infrastructure-plan')
# sd = sd_algorithm.SDAlgorithm()
# newPol4 = get_content('https://www.aljazeera.com/news/2021/4/2/fears-of-low-turnout-as-bulgaria-prepares-to-vote-in-pandemic')
# sd = sd_algorithm.SDAlgorithm()
# newPol5 = get_content('https://www.aljazeera.com/news/2021/4/5/putin-signs-law-allowing-him-two-more-terms-as-russias-leader')
# sd = sd_algorithm.SDAlgorithm()
# newPol6 = get_content('https://www.aljazeera.com/news/2021/4/6/russia-ups-security-at-navalny-prison-ahead-of-planned-protest')

# # Business and Economy news
# sd = sd_algorithm.SDAlgorithm()
# newBus1 = get_content('https://www.aljazeera.com/news/2021/4/6/lebanons-baalbek-reborn-temples-a-newly-launched-virtual-tour')
# sd = sd_algorithm.SDAlgorithm()
# newBus2 = get_content('https://www.aljazeera.com/economy/2021/4/6/jal-to-retire-fleet-of-planes-that-use-pratt-whitney-engines')
# sd = sd_algorithm.SDAlgorithm()
# newBus3 = get_content('https://www.aljazeera.com/economy/2021/4/5/race-to-the-bottom-yellen-makes-case-for-global-minimum-tax-rate')
# sd = sd_algorithm.SDAlgorithm()
# newBus4 = get_content('https://www.aljazeera.com/economy/2021/4/5/gamestop-plans-1bn-share-sale-after-reddit-fuelled-rally')
# sd = sd_algorithm.SDAlgorithm()
# newBus5 = get_content('https://www.aljazeera.com/economy/2021/4/5/global-stocks-rise-spurred-by-surge-in-us-employment-data')
# sd = sd_algorithm.SDAlgorithm()
# newBus6 = get_content('https://www.aljazeera.com/economy/2021/4/5/dow-hits-new-record-as-brightening-outlook-unleashes-bulls')

# # Sport news
# sd = sd_algorithm.SDAlgorithm()
# newSpo1 = get_content('https://www.aljazeera.com/sports/2021/3/28/pakistan-football-federation-office-attacked')
# sd = sd_algorithm.SDAlgorithm()
# newSpo2 = get_content('https://www.aljazeera.com/news/2021/3/27/indian-cricket-legend-tendulkar-tests-positive-for-coronavirus')
# sd = sd_algorithm.SDAlgorithm()
# newSpo3 = get_content('https://www.aljazeera.com/news/2021/3/26/football-star-thierry-henry-quitting-social-media-over-racism)
# sd = sd_algorithm.SDAlgorithm()
# newSpo4 = get_content('https://www.aljazeera.com/sports/2021/4/4/football-valencia-briefly-walk-off-pitch-after-alleged-racism')
# sd = sd_algorithm.SDAlgorithm()
# newSpo5 = get_content('https://www.aljazeera.com/news/2021/3/20/ncaa-slammed-for-inequality-between-mens-and-womens-facilities)
# sd = sd_algorithm.SDAlgorithm()
# newSpo6 = get_content('https://www.aljazeera.com/sports/2021/3/31/african-tribe-long-marginalised-in-india-seeks-sporting-glory')


# # Entertainment
# sd = sd_algorithm.SDAlgorithm()
# newEnt1 = get_content('https://www.aljazeera.com/economy/2021/4/2/us-court-orders-halt-to-satan-shoe-sales-in-nike-trademark-row')
# sd = sd_algorithm.SDAlgorithm()
# newEnt2 = get_content('https://www.aljazeera.com/economy/2021/3/19/the-fed-women-entrepreneurs-and-the-kardashians-long-goodbye')
# sd = sd_algorithm.SDAlgorithm()
# newEnt3 = get_content('https://www.aljazeera.com/news/2021/3/17/disneyland-to-reopen')
# sd = sd_algorithm.SDAlgorithm()
# newEnt4 = get_content('https://www.aljazeera.com/news/2021/3/15/beyonce-taylor-swift-make-history-as-women-dominate-grammys')
# sd = sd_algorithm.SDAlgorithm()
# newEnt5 = get_content('https://www.aljazeera.com/economy/2021/3/2/new-harry-potter-video-game-will-allow-trans-characters')
# sd = sd_algorithm.SDAlgorithm()
# newEnt6 = get_content('https://www.aljazeera.com/economy/2021/2/2/gamestop-stock-fizzles-80-from-last-weeks-spectacular-highs')


# """ Getting contents from The guardian """

# # Political news
# sd = sd_algorithm.SDAlgorithm()
# guaPol1 = get_content('https://www.theguardian.com/politics/2021/apr/06/keir-starmer-apologises-for-visiting-jesus-church-behind-which-performed-gay-exorcisms')
# sd = sd_algorithm.SDAlgorithm()
# guaPol2 = get_content('https://www.theguardian.com/environment/2021/apr/06/co2-from-englands-road-plan-up-to-100-times-more-than-dft-says')
# sd = sd_algorithm.SDAlgorithm()
# guaPol3 = get_content('https://www.theguardian.com/society/2021/apr/06/uk-long-covid-patients-facing-postcode-lottery-for-support')
# sd = sd_algorithm.SDAlgorithm()
# guaPol4 = get_content('https://www.theguardian.com/uk-news/2021/apr/05/conservative-mp-cheryl-gillan-dies-after-long-illness')
# sd = sd_algorithm.SDAlgorithm()
# guaPol5 = get_content('https://www.theguardian.com/politics/2021/apr/05/mayor-of-london-sadiq-khan-cannabis-legalisation-drugs-commission')
# sd = sd_algorithm.SDAlgorithm()
# guaPol6 = get_content('https://www.theguardian.com/world/2021/mar/30/who-criticises-chinas-data-sharing-as-it-releases-covid-origins-report')

# # Business news
# sd = sd_algorithm.SDAlgorithm()
# guaBus1 = get_content('https://www.theguardian.com/business/2021/apr/06/retail-entrepreneur-philip-day-backs-deal-to-keep-peacocks-afloat')
# sd = sd_algorithm.SDAlgorithm()
# guaBus2 = get_content('https://www.theguardian.com/travel/2021/apr/05/travel-industry-frustrated-by-lack-of-clarity-on-road-map-to-reopening')
# sd = sd_algorithm.SDAlgorithm()
# guaBus3 = get_content('https://www.theguardian.com/commentisfree/2021/mar/30/biden-tariffs-brexit-britain-eu-big-tech')
# sd = sd_algorithm.SDAlgorithm()
# guaBus4 = get_content('https://www.theguardian.com/business/2021/apr/06/uk-electric-car-sales-covid-lockdown')
# sd = sd_algorithm.SDAlgorithm()
# guaBus5 = get_content('https://www.theguardian.com/uk-news/2021/apr/05/how-a-food-bank-is-helping-city-service-workers-survive-the-pandemic')
# sd = sd_algorithm.SDAlgorithm()
# guaBus6 = get_content('https://www.theguardian.com/money/2021/mar/29/britons-pay-back-most-on-debt-in-27-years-as-credit-card-spending-slumps-covid')

# # Sport news
# sd = sd_algorithm.SDAlgorithm()
# guaSpo1 = get_content('https://www.theguardian.com/football/2021/apr/06/lille-win-psg-a-reminder-fame-ligue-1-france-title-race')
# sd = sd_algorithm.SDAlgorithm()
# guaSpo2 = get_content('https://www.theguardian.com/football/2021/apr/05/wolves-west-ham-premier-league-match-report')
# sd = sd_algorithm.SDAlgorithm()
# guaSpo3 = get_content('https://www.theguardian.com/football/2021/apr/05/ousmane-dembele-barcelona-real-valladolid-la-liga-el-clasico')
# sd = sd_algorithm.SDAlgorithm()
# guaSpo4 = get_content('https://www.theguardian.com/football/2021/apr/05/championship-middlesbrough-watford-swansea-preston-roundup')
# sd = sd_algorithm.SDAlgorithm()
# guaSpo5 = get_content('https://www.theguardian.com/football/football-league-blog/2021/apr/06/how-did-gillingham-become-the-only-efl-club-not-to-pay-agents-a-penny-football')
# sd = sd_algorithm.SDAlgorithm()
# guaSpo6 = get_content('https://www.theguardian.com/sport/2021/mar/24/british-masters-golf-bid-for-crowds-at-proposed-covid-pilot-event-in-may')


# # Entertainment
# sd = sd_algorithm.SDAlgorithm()
# guaEnt1 = get_content('https://www.theguardian.com/tv-and-radio/2021/apr/06/ainsley-harriott-i-talk-to-my-ingredients-when-im-cooking')
# sd = sd_algorithm.SDAlgorithm()
# guaEnt2 = get_content('https://www.theguardian.com/lifeandstyle/2021/apr/05/how-we-met-i-was-terrified-my-parents-would-find-out-id-been-intimate-with-another-girl')
# sd = sd_algorithm.SDAlgorithm()
# guaEnt3 = get_content('https://www.theguardian.com/film/2021/apr/06/terminator-rocky-godzilla-king-kong-versus-movie')
# sd = sd_algorithm.SDAlgorithm()
# guaEnt4 = get_content('https://www.theguardian.com/media/2021/apr/06/brilliant-and-versatile-observer-and-guardian-journalist-sarah-hughes-dies-at-48')
# sd = sd_algorithm.SDAlgorithm()
# guaEnt5 = get_content('https://www.theguardian.com/film/2021/apr/05/hear-me-out-why-serenity-isnt-a-bad-movie')
# sd = sd_algorithm.SDAlgorithm()
# guaEnt6 = get_content('https://www.theguardian.com/food/2021/apr/06/barbecues-are-back-ten-perfect-burgers-to-try-from-vegan-bean-to-bhaji-bites')










# # CBS News

# 'https://www.cbsnews.com/news/gottlieb-covid-infections-hot-spots-face-the-nation/',
#                       'https://www.cbsnews.com/news/evangelical-church-covid-19-pandemic-vaccine-skeptics/',
#                       'https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/',
#                       'https://www.cbsnews.com/news/capitol-riot-arrests-2021-04-02/',
#                       'https://www.cbsnews.com/news/william-evans-capitol-police-office-killed-lie-honor-rotunda/',
#                       'https://www.cbsnews.com/news/pelosi-matt-gaetz-removed-frobm-judiciary-committee-if-allegations-true/',
#                       'https://www.cbsnews.com/news/pet-adoption-surge-puppy-nannies-demand/',
#                       'https://www.cbsnews.com/news/supreme-court-sides-google-oracle-copyright-case/',
#                       'https://www.cbsnews.com/news/stimulus-check-veterans-waiting-payment/',
#                       'https://www.cbsnews.com/news/tax-increase-corporate-taxes-trump-biden/',
#                       'https://www.cbsnews.com/news/facebook-hack-500-million-accounts/',
#                       'https://www.cbsnews.com/news/corporate-tax-global-minimum-rate-yellen/',
#                       'https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/',
#                       'https://www.cbssports.com/college-basketball/news/scott-drew-never-let-others-change-his-story-path-or-program-and-thats-how-he-led-baylor-to-its-first-title/',
#                       'https://www.cbssports.com/golf/news/2021-masters-odds-favorites-why-you-should-root-for-these-nine-golfers-to-win-at-augusta-national/',
#                       'https://www.cbssports.com/wwe/news/wwe-raw-results-recap-grades-drew-mcintyre-bobby-lashley-stand-tall-ahead-of-wrestlemania-clash/live/',
#                       'https://www.cbssports.com/fantasy/baseball/news/fantasy-baseball-injury-reaction-fernando-tatis-likely-out-a-while-with-shoulder-subluxation-what-now/',
#                       'https://www.cbssports.com/college-basketball/news/2021-ncaa-tournament-bracket-college-basketball-scores-championship-game-schedule-stream-march-madness/',
#                       'https://www.cbsnews.com/news/dmx-hospital-vigil-family/',
#                       'https://www.cbsnews.com/news/music-and-the-medici/',
#                       'https://www.cbsnews.com/news/carrie-underwood-album-of-gospel-standards-my-savior/',
#                       'https://www.cbsnews.com/news/dmx-heart-attack-hospitalized/',
#                       'https://www.cbsnews.com/news/stanford-womens-ncaa-tournament-chamnpions-2021-arizona/',
#                       'https://www.cbsnews.com/news/bridgerton-star-rege-jean-page-duke-of-hastings-season-2/',



# #BBC
# #..............................

# 'https://www.bbc.com/news/uk-56645208','https://www.bbc.com/news/56129210','https://www.bbc.com/news/av/uk-politics-56646912',
# 'https://www.bbc.com/news/uk-politics-56647573','https://www.bbc.com/news/uk-northern-ireland-56644797','https://www.bbc.com/news/uk-wales-56611091',
# 'https://www.bbc.com/news/business-56644058','https://www.bbc.com/news/technology-56639088','https://www.bbc.com/news/business-56650685',
# 'https://www.bbc.com/news/business-56646761','https://www.bbc.com/news/business-52567567','https://www.bbc.com/news/business-54454990',
# 'https://www.bbc.com/sport/tennis/56649098','https://www.bbc.com/sport/tennis/56618948','https://www.bbc.com/sport/rugby-union/56650185',
# 'https://www.bbc.com/sport/football/56001747','https://www.bbc.com/sport/athletics/54964728','https://www.bbc.com/sport/athletics/51800436',
# 'https://www.bbc.com/culture/article/20191106-why-chinese-rappers-dont-fight-the-power','https://www.bbc.com/culture/article/20200218-the-best-james-bond-themes-that-never-made-it-to-the-screen',
# 'https://www.bbc.com/culture/article/20191007-the-greatest-hip-hop-songs-of-all-time','https://www.bbc.com/culture/article/20210329-remembering-miss-fury-the-worlds-first-great-superheroine',
# 'https://www.bbc.com/culture/article/20210305-caterina-van-hemessen-an-unknown-visual-pioneer','https://www.bbc.com/culture/article/20210326-how-african-fashion-has-conquered-film',

# #..............................


# #aljazeera
# #..............................

# 'https://www.aljazeera.com/news/2021/4/4/profile-who-is-jordans-prince-hamza',
# 'https://www.aljazeera.com/news/2021/4/6/israels-president-to-announce-candidate-to-form-new-government',
# 'https://www.aljazeera.com/news/2021/4/4/republican-senator-urges-scaled-down-us-infrastructure-plan',
# 'https://www.aljazeera.com/news/2021/4/2/fears-of-low-turnout-as-bulgaria-prepares-to-vote-in-pandemic',
# 'https://www.aljazeera.com/news/2021/4/5/putin-signs-law-allowing-him-two-more-terms-as-russias-leader',
# 'https://www.aljazeera.com/news/2021/4/6/russia-ups-security-at-navalny-prison-ahead-of-planned-protest',
# 'https://www.aljazeera.com/news/2021/4/6/lebanons-baalbek-reborn-temples-a-newly-launched-virtual-tour',
# 'https://www.aljazeera.com/economy/2021/4/6/jal-to-retire-fleet-of-planes-that-use-pratt-whitney-engines',
# 'https://www.aljazeera.com/economy/2021/4/5/race-to-the-bottom-yellen-makes-case-for-global-minimum-tax-rate',
# 'https://www.aljazeera.com/economy/2021/4/5/gamestop-plans-1bn-share-sale-after-reddit-fuelled-rally',
# 'https://www.aljazeera.com/economy/2021/4/5/global-stocks-rise-spurred-by-surge-in-us-employment-data',
# 'https://www.aljazeera.com/economy/2021/4/5/dow-hits-new-record-as-brightening-outlook-unleashes-bulls',
# 'https://www.aljazeera.com/sports/2021/3/28/pakistan-football-federation-office-attacked',
# 'https://www.aljazeera.com/news/2021/3/27/indian-cricket-legend-tendulkar-tests-positive-for-coronavirus',
# 'https://www.aljazeera.com/news/2021/3/26/football-star-thierry-henry-quitting-social-media-over-racism',
# 'https://www.aljazeera.com/sports/2021/4/4/football-valencia-briefly-walk-off-pitch-after-alleged-racism',
# 'https://www.aljazeera.com/news/2021/3/20/ncaa-slammed-for-inequality-between-mens-and-womens-facilities',
# 'https://www.aljazeera.com/sports/2021/3/31/african-tribe-long-marginalised-in-india-seeks-sporting-glory',
# 'https://www.aljazeera.com/economy/2021/4/2/us-court-orders-halt-to-satan-shoe-sales-in-nike-trademark-row',
# 'https://www.aljazeera.com/economy/2021/3/19/the-fed-women-entrepreneurs-and-the-kardashians-long-goodbye',
# 'https://www.aljazeera.com/news/2021/3/17/disneyland-to-reopen',
# 'https://www.aljazeera.com/news/2021/3/15/beyonce-taylor-swift-make-history-as-women-dominate-grammys',
# 'https://www.aljazeera.com/economy/2021/3/2/new-harry-potter-video-game-will-allow-trans-characters',
# 'https://www.aljazeera.com/economy/2021/2/2/gamestop-stock-fizzles-80-from-last-weeks-spectacular-highs',

# #..............................



# #The guardian
# #..............................

# 'https://www.theguardian.com/politics/2021/apr/06/keir-starmer-apologises-for-visiting-jesus-church-behind-which-performed-gay-exorcisms',
# 'https://www.theguardian.com/environment/2021/apr/06/co2-from-englands-road-plan-up-to-100-times-more-than-dft-says',
# 'https://www.theguardian.com/society/2021/apr/06/uk-long-covid-patients-facing-postcode-lottery-for-support',
# 'https://www.theguardian.com/uk-news/2021/apr/05/conservative-mp-cheryl-gillan-dies-after-long-illness')
# 'https://www.theguardian.com/politics/2021/apr/05/mayor-of-london-sadiq-khan-cannabis-legalisation-drugs-commission',
# 'https://www.theguardian.com/world/2021/mar/30/who-criticises-chinas-data-sharing-as-it-releases-covid-origins-report',
# 'https://www.theguardian.com/business/2021/apr/06/retail-entrepreneur-philip-day-backs-deal-to-keep-peacocks-afloat',
# 'https://www.theguardian.com/travel/2021/apr/05/travel-industry-frustrated-by-lack-of-clarity-on-road-map-to-reopening',
# 'https://www.theguardian.com/commentisfree/2021/mar/30/biden-tariffs-brexit-britain-eu-big-tech',
# 'https://www.theguardian.com/business/2021/apr/06/uk-electric-car-sales-covid-lockdown',
# 'https://www.theguardian.com/uk-news/2021/apr/05/how-a-food-bank-is-helping-city-service-workers-survive-the-pandemic',
# 'https://www.theguardian.com/money/2021/mar/29/britons-pay-back-most-on-debt-in-27-years-as-credit-card-spending-slumps-covid',
# 'https://www.theguardian.com/football/2021/apr/06/lille-win-psg-a-reminder-fame-ligue-1-france-title-race',
# 'https://www.theguardian.com/football/2021/apr/05/wolves-west-ham-premier-league-match-report',
# 'https://www.theguardian.com/football/2021/apr/05/ousmane-dembele-barcelona-real-valladolid-la-liga-el-clasico',
# 'https://www.theguardian.com/football/2021/apr/05/championship-middlesbrough-watford-swansea-preston-roundup',
# 'https://www.theguardian.com/football/football-league-blog/2021/apr/06/how-did-gillingham-become-the-only-efl-club-not-to-pay-agents-a-penny-football',
# 'https://www.theguardian.com/sport/2021/mar/24/british-masters-golf-bid-for-crowds-at-proposed-covid-pilot-event-in-may',
# 'https://www.theguardian.com/tv-and-radio/2021/apr/06/ainsley-harriott-i-talk-to-my-ingredients-when-im-cooking',
# 'https://www.theguardian.com/lifeandstyle/2021/apr/05/how-we-met-i-was-terrified-my-parents-would-find-out-id-been-intimate-with-another-girl',
# 'https://www.theguardian.com/film/2021/apr/06/terminator-rocky-godzilla-king-kong-versus-movie',
# 'https://www.theguardian.com/media/2021/apr/06/brilliant-and-versatile-observer-and-guardian-journalist-sarah-hughes-dies-at-48',
# 'https://www.theguardian.com/film/2021/apr/05/hear-me-out-why-serenity-isnt-a-bad-movie',
# 'https://www.theguardian.com/food/2021/apr/06/barbecues-are-back-ten-perfect-burgers-to-try-from-vegan-bean-to-bhaji-bites',





# #..................................

























# urls = ['https://www.bbc.com/news/uk-56572775', 'https://www.bbc.com/news/world-latin-america-56581131', 'tps://www.bbc.com/news/world-asia-39595989', 'https://www.bbc.com/news/technology-55569604','https://www.bbc.com/news/uk-northern-ireland-56566468',
#         'https://www.bbc.com/news/business-56581614','https://www.bbc.com/news/business-56441829','https://www.bbc.com/news/business-56578445','https://www.bbc.com/news/technology-56154543','https://www.bbc.com/news/business-56585697',
#         'https://www.bbc.com/sport/football/56505758','https://www.bbc.com/sport/football/56586894','https://www.bbc.com/sport/golf/56559194','https://www.bbc.com/sport/football/56584938','https://www.bbc.com/sport/formula1/56557657',
#         'https://www.bbc.com/culture/article/20210315-the-mystery-of-lost-rock-genius-lee-mavers','https://www.bbc.com/culture/article/20210219-why-pop-stars-are-having-prosthetic-makeovers','https://www.bbc.com/culture/article/20210216-the-forgotten-story-of-americas-first-black-superstars','https://www.bbc.com/culture/article/20200923-is-princes-sign-o-the-times-the-greatest-album-of-all-time','https://www.bbc.com/culture/article/20140924-was-hendrix-really-that-original',
#         'https://www.newtimes.co.rw/news/premier-ngirente-attends-car-president-touaderas-swearing-ceremony','https://www.newtimes.co.rw/news/nine-takeaways-tuesdays-covid-19-news-conference','https://www.newtimes.co.rw/opinions/rusesabaginas-arrest-international-law','https://www.newtimes.co.rw/news/kagame-stresses-need-modernizing-international-debt-architecture','https://www.newtimes.co.rw/international/japan-appoints-minister-loneliness-tackle-covid-induced-suicides',
#         'https://www.newtimes.co.rw/news/what-next-after-shareholders-agree-dissolve-crystal-telecom','https://www.newtimes.co.rw/news/going-green-volkswagen-rwanda-unveils-new-motor-charging-station','https://www.newtimes.co.rw/news/featured-bk-group-registered-rwf384bn-after-tax-profit-2020','https://www.newtimes.co.rw/news/rwanda-banks-tech-get-18-households-out-food-insecurity','https://www.newtimes.co.rw/opinions/editorial-increased-consumption-local-products-could-drive-recovery',
#         'https://www.newtimes.co.rw/sports/uci-assess-rwandas-bid-host-2025-road-cycling-championship','https://www.newtimes.co.rw/sports/basketball-nba-sets-date-inaugural-bal-tourney','https://www.newtimes.co.rw/sports/hertier-irasubiza-young-talent-dreams-becoming-big-star-local-football','https://www.newtimes.co.rw/sports/mugisha-could-miss-tour-du-rwanda-2021','https://www.newtimes.co.rw/sports/tasks-await-mukura-head-coach-rodolfo-zapata',
#         'https://www.newtimes.co.rw/entertainment/miss-talent-2021-umutoniwase-named-hdi-youth-ambassador','https://www.newtimes.co.rw/entertainment/close-stand-comedian-joshua','https://www.newtimes.co.rw/entertainment/trees-peace-movie-premiere-next-month','https://www.newtimes.co.rw/entertainment/celebrating-womens-creativity-artists-live-stream-concert','https://www.newtimes.co.rw/entertainment/grace-ingabire-crowned-miss-rwanda-2021',
#         'https://www.theguardian.com/world/2021/mar/30/who-criticises-chinas-data-sharing-as-it-releases-covid-origins-report','https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t','https://www.theguardian.com/uk-news/2021/mar/30/report-into-policing-of-sarah-everard-vigil-a-missed-opportunity','https://www.theguardian.com/education/2021/mar/30/ofsted-chief-asked-for-greater-powers-to-monitor-private-schools','https://www.theguardian.com/global-development/2021/mar/31/in-the-middle-of-a-war-zone-thousands-flee-as-venezuela-troops-and-colombia-rebels-clash',
#         'https://www.theguardian.com/business/2021/mar/30/infrastructure-projects-should-use-more-uk-steel-says-trade-body','https://www.theguardian.com/business/2021/mar/31/fullers-to-raise-cash-after-burning-through-up-to-5m-a-month-covid','https://www.theguardian.com/business/2021/mar/31/uk-economy-savings-expansion-recovery','https://www.theguardian.com/commentisfree/2021/mar/30/biden-tariffs-brexit-britain-eu-big-tech','https://www.theguardian.com/mocbs/2021/mar/29/britons-pay-back-most-on-debt-in-27-years-as-credit-card-spending-slumps-covid',
#         'https://www.theguardian.com/football/2021/mar/30/wales-czech-republic-world-cup-qualifier-match-report','https://www.theguardian.com/football/2021/mar/31/agents-ready-for-war-with-fifa-over-new-rules-raiola-barnett-football-forum','https://www.theguardian.com/football/2021/mar/31/trevoh-chalobah-lorient-chelsea-psg-mark-cbsmar','https://www.theguardian.com/football/2021/mar/30/fa-to-use-psychological-profiling-to-help-appoint-england-women-captain','https://www.theguardian.com/sport/2021/mar/24/british-masters-golf-bid-for-crowds-at-proposed-covid-pilot-event-in-may',
#         'https://www.theguardian.com/music/2021/mar/30/cardi-b-haircare-products-afro-latina-hair','https://www.theguardian.com/music/2021/mar/31/britney-spears-responds-to-documentary-about-her-life-framing','https://www.theguardian.com/music/2021/mar/30/antonio-pappano-to-replace-simon-rattle-at-london-symphony-orchestra','https://www.theguardian.com/music/2021/mar/30/lil-nas-x-montero-call-me-by-your-name-twitter','https://www.theguardian.com/culture/2021/mar/31/glastonbury-live-stream-festival-coldplay-michael-kiwanuka-and-haim-to-perform',
#         'https://www.nytimes.com/2021/03/29/us/politics/biden-virus-vaccine.html','https://www.nytimes.com/2021/03/30/us/politics/democrats-voting-rights-bill.html','https://www.nytimes.com/2021/03/31/us/politics/capitol-police-lawsuit-trump.html','https://www.nytimes.com/2021/03/31/us/supreme-court-ncaa.html','https://www.nytimes.com/2021/03/30/us/politics/blinken-human-rights-women.html',
#         'https://www.nytimes.com/2021/03/29/business/archegos-hwang-viacomney-discovery.html','https://www.nytimes.com/2021/03/30/business/ffel-student-loans-paused.html','https://www.nytimes.com/2021/03/27/at-home/how-to-save-at-the-grocery-store.html','https://www.nytimes.com/2021/03/20/style/spending-rich-people.html','https://www.nytimes.com/2021/03/12/your-mocbs/taxes/2020-taxes-work-from-home.html',
#         'https://www.nytimes.com/2021/03/26/sports/soccer/jesse-lingard-england-west-ham.html','https://www.nytimes.com/2021/03/30/sports/ncaabasketball/march-madness-final-four-gonzaga.html','https://www.nytimes.com/2021/03/31/sports/ncaabasketball/ncaa-womens-final-four-preview.html','https://www.nytimes.com/2021/03/31/sports/soccer/soccer-streetwear-juventus.html','https://www.nytimes.com/interactive/2021/03/29/sports/soccer/champions-league-new-format.html',
#         'https://www.nytimes.com/2021/03/29/arts/music/sasha-velour-drag-opera.html','https://www.nytimes.com/2021/03/29/style/arizona-marijuana-legalization.html','https://www.nytimes.com/2021/03/30/arts/music/freddie-redd-dead.html','https://www.nytimes.com/2021/03/29/arts/music/justin-bieber-justice-billboard-chart.html','https://www.nytimes.com/2021/03/28/arts/music/biggest-indoor-rock-concert-barcelona.html']
# # Entertainment
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt1 = get_content('https://www.nytimes.com/2021/03/29/arts/music/sasha-velour-drag-opera.html')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt2 = get_content('https://www.nytimes.com/2021/03/29/style/arizona-marijuana-legalization.html')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt3 = get_content('https://www.nytimes.com/2021/03/30/arts/music/freddie-redd-dead.html')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt4 = get_content('https://www.nytimes.com/2021/03/29/arts/music/justin-bieber-justice-billboard-chart.html')
# sd = sd_algorithm.SDAlgorithm()
# cbsEnt5 = get_content('https://www.nytimes.com/2021/03/28/arts/music/biggest-indoor-rock-concert-barcelona.html')

# """ Getting data into a dataframe """
# labels = ['politics', 'politics', 'politics', 'politics', 'politics', 'business', 'business', 'business', 'business', 'business', 
#           'sports', 'sports', 'sports', 'sports', 'sports', 'entertainment', 'entertainment', 'entertainment', 'entertainment', 'entertainment',
#           'politics', 'politics', 'politics', 'politics', 'politics', 'business', 'business', 'business', 'business', 'business', 
#           'sports', 'sports', 'sports', 'sports', 'sports', 'entertainment', 'entertainment', 'entertainment', 'entertainment', 'entertainment',
#           'politics', 'politics', 'politics', 'politics', 'politics', 'business', 'business', 'business', 'business', 'business', 
#           'sports', 'sports', 'sports', 'sports', 'sports', 'entertainment', 'entertainment', 'entertainment', 'entertainment', 'entertainment',
#           'politics', 'politics', 'politics', 'politics', 'politics', 'business', 'business', 'business', 'business', 'business', 
#           'sports', 'sports', 'sports', 'sports', 'sports', 'entertainment', 'entertainment', 'entertainment', 'entertainment', 'entertainment']



# dictionary = {"article":[bbcPol1, bbcPol2, bbcPol3, bbcPol4, bbcPol5, bbcBus1, bbcBus2, bbcBus3, bbcBus4, bbcBus5, 
#                          bbcSpo1, bbcSpo2, bbcSpo3, bbcSpo4, bbcSpo5, bbcEnt1, bbcEnt2, bbcEnt3, bbcEnt4, bbcEnt5, 
#                          newPol1, newPol2, newPol3, newPol4, newPol5, newBus1, newBus2, newBus3, newBus4, newBus5, 
#                          newSpo1, newSpo2, newSpo3, newSpo4, newSpo5, newEnt1, newSpo2, newSpo3, newSpo4, newSpo5, 
#                          guaPol1, guaPol2, guaPol3, guaPol4, guaPol5, guaBus1, guaBus2, guaBus3, guaBus4, guaBus5, 
#                          guaSpo1, guaSpo2, guaSpo3, guaSpo4, guaSpo5, guaEnt1, guaEnt2, guaEnt3, guaEnt4, guaEnt5, 
#                          cbsPol1, cbsPol2, cbsPol3, cbsPol4, cbsPol5, cbsBus1, cbsBus2, cbsBus3, cbsBus4, cbsBus5, 
#                          cbsSpo1, cbsSpo2, cbsSpo3, cbsSpo4, cbsSpo5, cbsEnt1, cbsEnt2, cbsEnt3, cbsEnt4, cbsEnt5, ], "category": labels, "url": urls}

# df = pd.DataFrame(dictionary)

df.to_csv("mined_news.csv")