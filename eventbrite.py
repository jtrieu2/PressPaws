import requests 
import os
import json




def get_eventbrite_details(city, num_events):
	EVENTBRITE_TOKEN = os.environ.get('EVENTBRITE_TOKEN')
	EVENTBRITE_URL = "https://www.eventbriteapi.com/v3/"
	headers = {'Authorization': 'Bearer ' + EVENTBRITE_TOKEN}

	payload=dict()
	payload['q'] = 'dog events'
	payload['location.address'] = city
	payload['location.within'] = '15mi'
	payload['sort_by'] = 'date'
	response = requests.get(EVENTBRITE_URL + "events/search/", params=payload, headers=headers)
	data = response.json()

	# use the list of events from the returned JSON
	if response.ok:
	    events = data['events']
	    # create a list of events based on id and plug this list into other endpoints to get the full event details
	else:
		print('broken')

	if response.ok:
	# this takes long to implement so creatae a batched request
		events = events[0:num_events]
		batched_search = []
		for event in events:
			event_id = event['id']
			print(event_id)
			search_key = {"method": "GET", "relative_url": f"events/{event_id}/?expand=venue"}
			batched_search.append(search_key)

		batched_request = json.dumps(batched_search)

		payload = {'batch': batched_request}

		response = requests.post(EVENTBRITE_URL + "batch/", params = payload, headers = headers)

		data=response.json()
		 
		events_list = []
		for el in data:
			event = json.loads(el['body'])
			events_list.append(event)

		filtered_event_list = []
		filtered_event_id_list = []
		for item in events_list:
			if item['logo']:
				event = {}
				event['event_id'] = item['id']
				event['event_name'] = item['name']['text']
				event['event_address'] = item['venue']['address']['localized_multi_line_address_display']
				event['eventbrite_url'] = item['url']
				event['event_date'] = (item['start']['local']).split('T')[0]
				event['event_image'] = item['logo']['original']['url']
				event['event_description'] = item['description']['html']
				filtered_event_list.append(event)
				filtered_event_id_list.append(item['id'])

		return [filtered_event_list, filtered_event_id_list]

def get_event_details(event_id):
	EVENTBRITE_TOKEN = os.environ.get('EVENTBRITE_TOKEN')
	EVENTBRITE_URL = "https://www.eventbriteapi.com/v3/"
	headers = {'Authorization': 'Bearer ' + EVENTBRITE_TOKEN}

	response = requests.get(EVENTBRITE_URL + f'events/{event_id}/?expand=venue', headers=headers)
	data = response.json()
	event_info = {}
	if response.ok: 
		event_info['event_id'] = data['id']
		event_info['event_name'] = data['name']['text']
		event_info['event_address'] = data['venue']['address']['localized_address_display']
		event_info['eventbrite_url'] = data['url']
		event_info['event_date'] = (data['start']['local']).split('T')[0]
		event_info['event_image'] = data['logo']['original']['url']
		event_info['event_description'] = data['description']['html']

	return event_info






