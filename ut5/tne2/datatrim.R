library(tidyverse)

TARGET_YEAR <- 2019

matches <- read_csv('files/full_matches.csv') |>
  filter(year == TARGET_YEAR) |>
  select(
    match_id,
    tournament,
    date,
    round,
    duration = match_minutes
  ) |> 
  drop_na()

stats <- read_csv('files/full_stats.csv') |>
  select(
    match_id,
    player_id,
    winner
  ) |>
  filter(match_id %in% matches$match_id) |>
  drop_na() |>
  arrange(match_id)

players <- read_csv('files/full_players.csv') |>
  filter(player_id %in% stats$player_id) |>
  select(
    player_id,
    name,
    hand,
    country,
    birthdate = birthday
  ) |>
  mutate(
    hand = ifelse(hand == 'U', sample(c('R', 'L')), hand)
  ) |>
  drop_na()

matches |>
  write_csv('files/matches.csv')

stats |>
  write_csv('files/stats.csv')

players |>
  write_csv('files/players.csv')