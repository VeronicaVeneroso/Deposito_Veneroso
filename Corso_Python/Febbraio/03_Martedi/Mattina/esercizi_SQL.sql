-- mostra tutta la tabella film
select * from film;

-- mostra solo la colonna phone della tabella address
select phone from address;

-- mostra le colonne rental_id e amount delle righe in cui amount è pari a 0.99
select rental_id, amount from payment
where amount = 0.99;

-- mostra le colonne rental_id e amount delle righe in cui amount è superiore a 4
select rental_id, amount from payment
where amount > 4;

-- Mostra i film in ordine decrescente di lunghezza
select * from film
order by length DESC;

-- Mostra i primi 10 film dell'elenco di film in ordine decrescente di lunghezza
select * from film
order by length DESC
LIMIT 10;

-- ricerca titoli con la sequenza "aby" nel titolo
select * from film
where title like "%aby%";

-- Mostra film con lunghezza maggiore di 120 e rental_rate < 10
select * from film
where length > 120 AND rental_rate < 10;

-- Mostra i film con lunghezza > 120 e < 60
select * from film
where length > 120 OR length < 60;

-- Mostra i film con lunghezza compresa tra 60 e 90
select * from film
where length between 60 and 90;

-- Mostra i film con rating G o R
select * from film
where rating IN ("G", "R");

-- Mostra tutti i valori possibili di rental_rate
select distinct rental_rate from film;

-- Conta il numero di film presenti in tabella
select count(*) from film;

-- Conta quanti film ci sono per ogni tipo di rating (si può fare senza as con la stringa)
select rating, count(*) as totale_film
from film
group by rating;

select customer_id, SUM(amount) as totale_speso
from payment
group by customer_id;


-- Estrai i nomi (first_name) e i cognomi (last_name) di tutti gli attori presenti nella tabella actor.
-- Rinomina le colonne come "Nome" e "Cognome" per rendere il report più leggibile.
select first_name as Nome, last_name as Cognome
from actor;

-- Trova tutti i titoli dei film che hanno un rating uguale a 'G' (General Audiences).
select * from film
where rating = "G";

-- Trova tutti i clienti nella tabella customer
-- il cui nome inizia con la lettera "A" e il cognome finisce con la lettera "S".
select * from
where first_name like "A%" AND last_name like "%S";

-- Seleziona i film che hanno una durata (length) superiore
-- a 150 minuti E un costo di noleggio (rental_rate) inferiore a 1.00$.
select * from film
where length>150 AND rental_rate < 1;

-- Mostra i 10 film più lunghi presenti nel database,
-- ordinandoli dal più lungo al più corto.
select * from film
order by length DESC
LIMIT 10;

-- Qual è il prezzo medio di noleggio (rental_rate) di tutti i film?
-- Rinomina il risultato come "Prezzo_Medio_Noleggio".
select avg(rental_rate) as Prezzo_Medio_Noleggio from film;

-- Nella tabella film, conta quanti film ci sono per ogni durata di noleggio
-- (rental_duration).
select rental_duration as durata_noleggio, count(*) as numero_film
from film
group by rental_duration;

-- Vai nella tabella payment e conta quanti pagamenti ha registrato ogni staff_id.
select staff_id, count(*) as totale_pagamenti
from payment
group by staff_id;

-- Per ogni customer_id nella tabella payment, mostra il pagamento più alto (MAX)
-- e quello più basso (MIN) che abbiano mai effettuato.
select customer_id, MAX(amount) AS pagamento_massimo,
    MIN(amount) AS pagamento_minimo
from payment
group by customer_id;