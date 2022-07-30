import CustomSelect from "./Select";
import { movieSearch } from "../api/search";
import {
  Button,
  Card,
  Center,
  Grid,
  Group,
  List,
  Paper,
  Stack,
  TextInput,
} from "@mantine/core";
import { Hit } from "../types/movie";
import { useState } from "react";

const Search = () => {
  const [movies, setMovies] = useState<Hit[]>([]);
  const loadOptions = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.currentTarget.value;

    const data = await movieSearch({
      keyword: value,
    });
    if (!data) {
      setMovies([]);
      return;
    }
    setMovies(data.hits?.hits || []);
  };
  return (
    <Center>
      <Paper shadow="xs" p="md">
        <Group
          grow
          sx={{
            width: "300px",
          }}
        >
          <TextInput label="Search" onChange={loadOptions} />
        </Group>
        {movies.length >= 0 &&
          movies.map((movie) => (
            <List key={`movie-${movie._source.title}`}>
              <List.Item>{movie._source.title}</List.Item>
            </List>
          ))}
      </Paper>
    </Center>
  );
};

export default Search;
