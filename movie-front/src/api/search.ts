import axios from "axios";
import { MovieSearchResult } from "../types/movie";

export const searchApi = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const movieSearch = async (input: Record<string, any>) => {
  try {
    console.log(input); //movies/_search
    const req = await searchApi.post<MovieSearchResult>("/", input, {});
    console.log(req.data);
    return req.data;
  } catch (error) {
    console.error(error);
  }
};
