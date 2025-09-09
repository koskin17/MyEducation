import { SearchIcon } from "lucide-react";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

interface SearchProps {
  onSubmit?: () => void;
}

export const Search = ({ onSubmit }: SearchProps) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [search, setSearch] = useState("");

  const handleSubmitSearch = () => {
    const trimmed = search.trim();
    if (!trimmed && searchParams.get("search")) {
      searchParams.delete("search");
      setSearchParams(searchParams);
      return;
    }
    const currentSearch = searchParams.get("search") ?? "";
    if (trimmed && trimmed !== currentSearch) {
      setSearchParams({ search: trimmed });
      onSubmit?.()
    }
  };

  useEffect(() => {
    const param = searchParams.get("search") ?? "";
    setSearch(param);
  }, [searchParams]);

  return (
    <div className="border border-inactive-100 rounded-sm flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]">
      <Input
        placeholder="Пошук"
        value={search}
        onChange={(ev) => setSearch(ev.target.value)}
        onKeyDown={(ev) => {
          if (ev.key === "Enter") {
            handleSubmitSearch();
          }
        }}
        className="border-none my-[1px] shadow-none outline-0 focus-visible:ring-0 px-2 placeholder:text-main-gray-90 font-display font-light"
      />
      <div className="border-l border-inactive-100">
        <Button
          onClick={handleSubmitSearch}
          variant={"tertiary"}
          className="p-3"
          aria-label="Search icon"
          disabled={searchParams.get("search") === search.trim()}
        >
          <SearchIcon />
        </Button>
      </div>
    </div>
  );
};
