--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7 (Ubuntu 10.7-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.7 (Ubuntu 10.7-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: avatars; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.avatars (
    avatar_id integer NOT NULL,
    url character varying(300)
);


ALTER TABLE public.avatars OWNER TO vagrant;

--
-- Name: avatars_avatar_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.avatars_avatar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avatars_avatar_id_seq OWNER TO vagrant;

--
-- Name: avatars_avatar_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.avatars_avatar_id_seq OWNED BY public.avatars.avatar_id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.events (
    event_id integer NOT NULL,
    user_id integer,
    eventbrite_id character varying(500),
    event_name character varying(300),
    event_address character varying(500),
    event_date character varying(100),
    "event_imURL" character varying(1000),
    event_website character varying(1000)
);


ALTER TABLE public.events OWNER TO vagrant;

--
-- Name: events_event_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.events_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_event_id_seq OWNER TO vagrant;

--
-- Name: events_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.events_event_id_seq OWNED BY public.events.event_id;


--
-- Name: places; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.places (
    place_id integer NOT NULL,
    user_id integer,
    place_name character varying(300),
    place_address character varying(500),
    "place_imURL" character varying(1000),
    place_website character varying(1000),
    place_hours character varying(1000)
);


ALTER TABLE public.places OWNER TO vagrant;

--
-- Name: places_place_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.places_place_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.places_place_id_seq OWNER TO vagrant;

--
-- Name: places_place_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.places_place_id_seq OWNED BY public.places.place_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying(64),
    lname character varying(64),
    email character varying(64),
    password character varying(64),
    zipcode character varying(15),
    url character varying(300)
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: avatars avatar_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.avatars ALTER COLUMN avatar_id SET DEFAULT nextval('public.avatars_avatar_id_seq'::regclass);


--
-- Name: events event_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events ALTER COLUMN event_id SET DEFAULT nextval('public.events_event_id_seq'::regclass);


--
-- Name: places place_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.places ALTER COLUMN place_id SET DEFAULT nextval('public.places_place_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: avatars; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.avatars (avatar_id, url) FROM stdin;
1	https://images.unsplash.com/photo-1505628346881-b72b27e84530?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=alan-king-380383-unsplash.jpg
2	https://images.unsplash.com/photo-1551717743-49959800b1f6?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=anya-potsiadlo-1412522-unsplash.jpg
3	https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=charles-540415-unsplash.jpg
4	https://images.unsplash.com/photo-1517849845537-4d257902454a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=charles-547196-unsplash.jpg
5	https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=charles-550068-unsplash.jpg
6	https://images.unsplash.com/photo-1534983283799-b12a2ad6b1a6?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=cyndi-perezita-790480-unsplash.jpg
7	https://images.unsplash.com/photo-1535311310-78aa1fc96804?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=evelyn-cespedes-795054-unsplash.jpg
8	https://images.unsplash.com/photo-1553998495-15606c6cb6f7?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=graham-holtshausen-1476744-unsplash.jpg
9	https://images.unsplash.com/photo-1524527847659-de3af4eff838?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=ian-espinosa-641435-unsplash.jpg
10	https://images.unsplash.com/photo-1504595403659-9088ce801e29?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jay-wennington-364037-unsplash.jpg
11	https://images.unsplash.com/photo-1510679674848-ee62d0e08ab9?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=marko-blazevic-447504-unsplash.jpg
12	https://images.unsplash.com/photo-1550469434-2e20fe65dad1?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=paul-thomas-1375986-unsplash.jpg
13	https://images.unsplash.com/photo-1499938971550-7ad287075e0d?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=sneaky-elbow-310084-unsplash.jpg
14	https://images.unsplash.com/photo-1505044024939-c154d39ca595?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=the-poodle-gang-369916-unsplash.jpg
15	https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=vincent-van-zalinge-1137995-unsplash.jpg
16	https://images.unsplash.com/photo-1518887371124-412923b6ccff?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=vitor-fontes-563168-unsplash.jpg
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.events (event_id, user_id, eventbrite_id, event_name, event_address, event_date, "event_imURL", event_website) FROM stdin;
1	1	1234asdf	Doggy Dayzz	200 Main St, San Francisco, CA 94110	January 1, 2019	https://images.unsplash.com/photo-1537151672256-6caf2e9f8c95?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=ipet-photo-1061142-unsplash.jpg	\N
2	1	45919956827	Group Volunteering	2253 Shafter Ave. , San Francisco, CA 94124	Jun 12, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F23127491%2F8252434483%2F1%2Foriginal.jpg?auto=compress&s=a96e36ddc34f776a6e509d2621654ac3	https://www.eventbrite.com/e/group-volunteering-tickets-45919956827
3	1	53272816428	Free Tour of SFPUC Headquarters Building at 525 Golden Gate Ave in SF	525 Golden Gate Avenue, San Francisco, CA 94102	Jun 12, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F53513016%2F29058883195%2F1%2Foriginal.jpg?auto=compress&s=141fa0ef83f2b117076de10ed2033ad4	https://www.eventbrite.com/e/free-tour-of-sfpuc-headquarters-building-at-525-golden-gate-ave-in-sf-registration-53272816428
4	1	59631723089	[FREE] Be someone else for a day	San Francisco	Jun 12, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F55706884%2F281261972775%2F1%2Foriginal.20190125-081658?auto=compress&s=8c07d7f8a883f3ce9bda90feddfb705e	https://www.eventbrite.com/e/free-be-someone-else-for-a-day-tickets-59631723089
5	1	62897803022	Grand Opening of Red Bay Coffee - San Francisco with Daily Driver	2535 3rd St, San Francisco, CA 94107	Jun 15, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F63479582%2F170826261530%2F1%2Foriginal.20190606-075051?auto=compress&s=437c969de7db6562061bf4238abf38f0	https://www.eventbrite.com/e/grand-opening-of-red-bay-coffee-san-francisco-with-daily-driver-tickets-62897803022
7	1	55813621043	The Buck	Broadway, Oakland, CA 94607	Jun 16, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F56132082%2F201392122239%2F1%2Foriginal.20190202-024038?auto=compress&s=858b9ffc4964ebd825db00dd73347f45	https://www.eventbrite.com/e/the-buck-tickets-55813621043
8	1	61906010544	Kate Quinn Literary Luncheon	276 Village Square, Orinda, CA 94563	Jun 17, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F62289294%2F90841235369%2F1%2Foriginal.20190514-223747?auto=compress&s=f406b3b0c4ae4a7f04f48c7a298c7567	https://www.eventbrite.com/e/kate-quinn-literary-luncheon-tickets-61906010544
11	1	62290520624	DIVAS NIGHT OUT Male Revue San Francisco! June 2019 with MEN OF EXOTICA	490 Broadway , San Francisco, CA 94133	Jun 15, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F62748056%2F14683897775%2F1%2Foriginal.20190523-003144?auto=compress&s=2416331f24d13765ad5134e452b157bc	https://www.eventbrite.com/e/divas-night-out-male-revue-san-francisco-june-2019-with-men-of-exotica-tickets-62290520624
12	1	59252941142	In-Shelter Volunteer Orientation at FDR	San Francisco, CA 94124	Jun 15, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F39316328%2F8252434483%2F1%2Foriginal.jpg?auto=compress&s=a8982f6a86ce271f8fff60fd4fe689f4	https://www.eventbrite.com/e/in-shelter-volunteer-orientation-at-fdr-registration-59252941142
13	1	62578839995	NISF Summer Hike @ Buena Vista Park	Haight & Buena Vista Ave Way, San Francisco, CA 94117	Jun 15, 2019	https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F63056543%2F590634703%2F1%2Foriginal.20190529-135831?auto=compress&s=68e89579daea1fdcb3aee2cb34f1ac2d	https://www.eventbrite.com/e/nisf-summer-hike-buena-vista-park-tickets-62578839995
\.


--
-- Data for Name: places; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.places (place_id, user_id, place_name, place_address, "place_imURL", place_website, place_hours) FROM stdin;
1	1	WinterWonderland	100 Main St, San Francisco, CA 94110	https://images.unsplash.com/photo-1537151672256-6caf2e9f8c95?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=ipet-photo-1061142-unsplash.jpg	\N	\N
2	1	Berkeley Humane	2700 Ninth Street, Berkeley, CA 94710, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAAQaZn4VgNHf0tzkP8aiTROGY3F3h48BWFDFEz9e7k79IaiHY_Z1-SCxCpy_Hl8oNOH5n3efS-v0iwBeVx1mV4ZFzeImbssVkkuFUEM4EAPTiodH86dRCQ7rd1N1sV57MHEhC874JbWs-Vh4-RMKRAnXrhGhQ6RcKM7BNRde6wRPyrmZDfFPpDig&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=32758	http://www.berkeleyhumane.org/	["Monday: Closed","Tuesday: Closed","Wednesday: Closed","Thursday: Closed","Friday: 11:00 AM – 5:00 PM","Saturday: 11:00 AM – 5:00 PM","Sunday: 11:00 AM – 5:00 PM"]
3	1	Peninsula Humane Society & SPCA Adoption Center	1450 Rollins Rd, Burlingame, CA 94010, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAATbXYeoeJ0xSS33lKSiYzkXPj6mVAMBUWdzYYKV8exDcY9DA7CBiFEAWD30iTRCUNkPLxUOQqva78BXIbv0BCMe3NUxH7JosHgo7xDrllNFm31PWOOsXAgaDOCZlLRlnREhDPS1PGmwzAYq-Q2wbv_pKCGhShRWNnHl5IAyLWVPj1LJCs8gb4Kw&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=52935	http://phs-spca.org/	["Monday: 11:00 AM – 7:00 PM","Tuesday: 11:00 AM – 7:00 PM","Wednesday: 11:00 AM – 7:00 PM","Thursday: 11:00 AM – 7:00 PM","Friday: 11:00 AM – 7:00 PM","Saturday: 11:00 AM – 6:00 PM","Sunday: 11:00 AM – 6:00 PM"]
6	1	Animal Haven	200 Centre St, New York, NY 10013, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAA5b73A6QcZuoJx9DHsOrQQ70K4VwR2LdKrjYbP_EmYoaSysozNy_Vq1oKg95oSbP81x3mwSLlzBT260tXW3ECJOaoj3kRdVHLgwKlyauaVZhWsQXT-giMRf-RzsGolMhtEhAdNGp4pY0l6xL13KCAcQoCGhR8JFCD7TXM_SIzgITr52_UKt9Hlw&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=77436	http://www.animalhavenshelter.org/	["Monday: Closed","Tuesday: 12:00 – 7:00 PM","Wednesday: 12:00 – 7:00 PM","Thursday: 12:00 – 7:00 PM","Friday: 12:00 – 7:00 PM","Saturday: 12:00 – 7:00 PM","Sunday: 12:00 – 7:00 PM"]
8	1	Animals Asia Foundation	300 Broadway #32, San Francisco, CA 94133, USA	https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jamie-street-804226-unsplash.jpg	http://www.animalsasia.org/	["Monday: 9:00 AM – 5:00 PM","Tuesday: 9:00 AM – 5:00 PM","Wednesday: 9:00 AM – 5:00 PM","Thursday: 9:00 AM – 5:00 PM","Friday: 9:00 AM – 5:00 PM","Saturday: Closed","Sunday: Closed"]
9	1	San Francisco SPCA Pacific Heights Adoption Center	2343 Fillmore St, San Francisco, CA 94115, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAAqf_TkzrEgV-mNw0xjSiqw_A9Mbsml0clnueFSH3fbDFoV2pVRYmpD-ynylE86_5RCv-o_EH_-KoJHtBKBCEFB5jj_QBE9PKYN7AJXrJhQAXMLsVdI6L4nv_yC6vj9bWNEhDlt86GjvKw-V11icYhDFK2GhTnf1jvw9_p2q145g8glqc4Vi1EPg&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=1530	http://www.sfspca.org/	["Monday: Open 24 hours","Tuesday: Open 24 hours","Wednesday: Open 24 hours","Thursday: Open 24 hours","Friday: Open 24 hours","Saturday: Open 24 hours","Sunday: Open 24 hours"]
13	1	Homeless Animal Adoption League, Inc.	236 Delawanna Ave, Clifton, NJ 07014, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAADxdeI_rBPeXdeViMSHvH0JoEmXVTGlMRgyIsn7GAm5EjPtogi9uFBmaoSWHzbIgDgz3cDr4ZR_QaoZN5mYcNMr4oaiwGqzbpZLThDayUCu1hRYZNbjVdQ39BBxVbhaPnEhBKGEgRvWRWZaJ8CJXtDNUpGhSM6Fkx8DuZP-MU1fv_1amuj8qE0A&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=116670	http://www.haalnj.org/	["Monday: Closed","Tuesday: Closed","Wednesday: 6:00 – 8:00 PM","Thursday: Closed","Friday: Closed","Saturday: 12:00 – 4:00 PM","Sunday: 10:00 AM – 2:00 PM"]
15	1	Animal Care Centers of NYC - Manhattan	326 E 110th St, New York, NY 10029, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAAXoz8uUE002iUu8LeuxhFLV6zFhLxAvpFpcdmYe2_FB_KZc7qvLrKCw3W8fRBOv8yPhRSIiohQx_OifUJIqhCZYtA97FUvyZfWlhfE1YGG219fMr2kr5DHf8pjtXa-j2FEhBCJ3Gv3Tr_332F56WYhwn9GhTgZd1FtKYti30nRZTsc4B8GNQywQ&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=4766	https://www.nycacc.org/Locations.htm	["Monday: 12:00 – 8:00 PM","Tuesday: 12:00 – 8:00 PM","Wednesday: 12:00 – 8:00 PM","Thursday: 12:00 – 8:00 PM","Friday: 12:00 – 8:00 PM","Saturday: 10:00 AM – 6:00 PM","Sunday: 10:00 AM – 6:00 PM"]
17	1	ASPCA C.A.R.E and Kitten Nursery	415 E 91st St, New York, NY 10128, USA	https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jamie-street-804226-unsplash.jpg	http://www.aspca.org/	["Monday: 7:00 AM – 11:00 PM","Tuesday: 7:00 AM – 11:00 PM","Wednesday: 7:00 AM – 11:00 PM","Thursday: 7:00 AM – 11:00 PM","Friday: 7:00 AM – 11:00 PM","Saturday: 7:00 AM – 11:00 PM","Sunday: 7:00 AM – 11:00 PM"]
18	1	Wonder Dog Rescue	2926 16th St, San Francisco, CA 94103, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAAMxQSU3Gu65ucQlvkuWfK9Yk9yMeynzM2pfma9--EAWpE4ZGANNjvpSTz8RkRVrwg3vKqbcPVJQougSyAFHFUeR4R78n46j7Y65RIC4pgat62sxaqb-RZfK-9ZoPEj4a_EhBBiBUlsB-EEy4c1UyP0IPRGhQmn-MyF1ZhMtzF9YlVBMFJ71HI0A&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=126877	http://www.wonderdogrescue.org/	["Monday: 10:00 AM – 4:00 PM","Tuesday: 10:00 AM – 4:00 PM","Wednesday: 10:00 AM – 4:00 PM","Thursday: 10:00 AM – 4:00 PM","Friday: 10:00 AM – 4:00 PM","Saturday: Closed","Sunday: Closed"]
19	1	New York City Siamese Rescue	New York, NY 10163, USA	https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jamie-street-804226-unsplash.jpg	http://nycsiamese.webs.com/	["Monday: Closed","Tuesday: Closed","Wednesday: Closed","Thursday: Closed","Friday: Closed","Saturday: Closed","Sunday: 1:00 – 3:00 PM"]
20	1	Bideawee	410 E 38th St, New York, NY 10016, USA	https://maps.googleapis.com/maps/api/place/js/PhotoService.GetPhoto?1sCmRaAAAAbc3jiV62Mab54WS6oYKzjJfB1UkDkKUqw8ecgUsnKWyaN8AJ_2xdGQ9kJRE81gdzYwqUo0XfQO9PpQYS52obl_fVIhds-8U4i08dX8CCsvoVwiIGAVtq7W2H6QtmjD26EhCidjCqR3GZo7D1S7bQ1nV6GhQLKMxspjZbUj0NlDK7-W5XfywAyg&3u200&4u200&5m1&2e1&callback=none&key=AIzaSyC_TMPIKWxlpfviB-hQI3DUujoDyG3nU6w&token=40834	http://bideawee.org/	["Monday: Closed","Tuesday: 11:00 AM – 7:00 PM","Wednesday: 11:00 AM – 7:00 PM","Thursday: 11:00 AM – 7:00 PM","Friday: 11:00 AM – 7:00 PM","Saturday: 11:00 AM – 6:00 PM","Sunday: 11:00 AM – 5:00 PM"]
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, fname, lname, email, password, zipcode, url) FROM stdin;
3	Tom	Jerry	tomandjerry@gmail.com	evil	evil	\N
1	Jenny	Trieu	jennytrieu10@gmail.com	evil	\N	https://images.unsplash.com/photo-1518887371124-412923b6ccff?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=vitor-fontes-563168-unsplash.jpg
\.


--
-- Name: avatars_avatar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.avatars_avatar_id_seq', 16, true);


--
-- Name: events_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.events_event_id_seq', 13, true);


--
-- Name: places_place_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.places_place_id_seq', 22, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- Name: avatars avatars_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.avatars
    ADD CONSTRAINT avatars_pkey PRIMARY KEY (avatar_id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (event_id);


--
-- Name: places places_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.places
    ADD CONSTRAINT places_pkey PRIMARY KEY (place_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: events events_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: places places_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.places
    ADD CONSTRAINT places_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

