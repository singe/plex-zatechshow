from datetime import datetime
from email.utils import parsedate

zatechshow_FEED_URL      = 'http://zatech.co.za/zats_mp4.xml'
zatechshow_ICON          = 'icon-default.png'
zatechshow_ART           = 'art-default.png'

###############################################################################
def Start():
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    MediaContainer.title1 = L('zatechshow')
    MediaContainer.art    = R(zatechshow_ART)
    HTTP.CacheTime        = CACHE_1HOUR

@handler('/video/zatechshow', L('zatechshow'))
def VideoMenu():
    dir = MediaContainer(mediaType='video', viewGroup='Details')
    episodes = RSS.FeedFromURL(zatechshow_FEED_URL)
    #thumb = episodes.channel.image.url
    thumb = "http://www.zatechshow.co.za/zats_cover.jpg"
    for episode in episodes['items']:
        try:
            for link in episode.links:
                if link.type == "audio/mpeg":
                    url = link.href
                else:
                    continue
            title    = episode.title
            date     = episode.updated
            duration = episode.itunes_duration
            summary  = episode.summary+"\n\nDuration: "+duration+"\nDate: "+date
            dir.Append(VideoItem(url, title=title, summary=summary, thumb=thumb, subtitle=date, duration=duration))
        except AttributeError:
            Log("Something odd with episode, skipping: %s" %episode)
    return dir
