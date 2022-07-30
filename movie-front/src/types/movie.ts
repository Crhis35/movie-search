export interface MovieSearchResult {
  took: number;
  timed_out: boolean;
  _shards: Shards;
  hits: Hits;
}

export interface Shards {
  total: number;
  successful: number;
  skipped: number;
  failed: number;
}

export interface Hits {
  total: Total;
  max_score: number;
  hits: Hit[];
}

export interface Hit {
  _index: Index;
  _id: string;
  _score: number;
  _source: Source;
}

export enum Index {
  Movies = "movies",
}

export interface Source {
  title: string;
  genres: string;
  search_index: string;
}

export interface Total {
  value: number;
  relation: string;
}
