# Networking_Strategies_Tracker.py

import pandas as pd

# Define all networking strategies
strategies = [
    'Cold emails to HR', 'Cold emails to Hiring Manager', 'Cold emails to Founder', 'Cold emails to Team Lead',
    'LinkedIn connection requests', 'LinkedIn messages after connection', 'LinkedIn InMail', 'LinkedIn group messages',
    'LinkedIn post comments', 'LinkedIn story interactions', 'LinkedIn endorsements + follow-up', 'LinkedIn recommendation request',
    'Twitter DMs to professionals', 'Twitter @mentions', 'Twitter thread interactions', 'Replying to tweets',
    'Instagram DMs', 'Instagram story interactions', 'Instagram commenting', 'Facebook group networking',
    'Careers page application', 'Contact-us form', 'Job board application', 'Referral program applications',
    'Submitting work samples/portfolio', 'Follow up after applications', 'Post-interview follow up', 'Niche industry portal applications',
    'Freelance project proposals', 'Internship/apprenticeship applications',
    'Industry conferences', 'Workshops/seminars', 'Webinars Q&A participation', 'Meetup groups', 'Hackathons', 'Job fairs',
    'Alumni meetups', 'Professional association meetings', 'Networking dinners', 'Speed networking events', 'Panel discussion interactions',
    'Speaking at events', 'Volunteering at events', 'Startup expos/demo days', 'Trade shows',
    'Online forums (Reddit, Discord, Slack)', 'Slack channels', 'Discord communities', 'Niche Facebook groups',
    'WhatsApp professional groups', 'Telegram groups', 'Commenting on blogs', 'Contributing to newsletters', 'Open-source communities',
    'Professional memberships', 'Writing LinkedIn articles', 'Blog posts on Medium', 'Guest blogging', 'YouTube content',
    'Podcasts', 'Twitter threads on expertise', 'Case studies', 'Sharing projects on GitHub/Behance', 'Slide decks on SlideShare', 'Research insights',
    'Asking friends for introductions', 'Asking colleagues for introductions', 'Asking alumni for guidance', 'Mentorship programs',
    'Asking clients for referrals', 'Asking partners/vendors for intros', 'LinkedIn mutual connections', 'Informational interviews',
    'Coffee chats', 'Networking lunches',
    'Offering free advice to companies', 'Offering freelance help', 'Portfolio review/feedback', 'Sharing relevant resources',
    'Congratulatory notes', 'Sharing job opportunities', 'Providing testimonials', 'Connecting two professionals',
    'Giving short case study to showcase skills', 'Thoughtful LinkedIn comments',
    'Optimizing LinkedIn profile', 'Optimizing personal website', 'Sharing project demos', 'Posting updates about work',
    'Publishing thought leadership content', 'Creating a newsletter', 'Public speaking', 'Twitter Spaces', 'Hosting/attending webinars', 'Podcast guest appearances',
    'Following up after a meeting', 'Following up after a webinar', 'Following up after a conference',
    'Reconnecting after no contact', 'Holiday/new-year greetings', 'Congratulating on awards/achievements', 'Sharing progress updates'
]

# Create DataFrame
data = {
    'Strategy': strategies,
    'Date': ['']*len(strategies),        # Empty cells for date
    'Completed': [False]*len(strategies), # For tick box in Sheets/Excel
    'Contact Name': ['']*len(strategies),
    'Contact Number': ['']*len(strategies)
}

df = pd.DataFrame(data)

# Save to Excel
file_name = 'Networking_Strategies_Tracker_Full.xlsx'
df.to_excel(file_name, index=False)
print(f"Excel tracker generated: {file_name}")
