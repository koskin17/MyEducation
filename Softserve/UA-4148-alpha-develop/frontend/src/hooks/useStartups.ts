import { getStartups } from "@/api/startups";
import type { IStartup } from "@/components/composed_ui/StartupCard";
import { useQuery } from "@tanstack/react-query";
import type { AxiosError } from "axios";

export function useStartups() {
  return useQuery<IStartup[], AxiosError<{ detail: string }>>({
    queryKey: ["startups"],
    queryFn: getStartups,
  });
}
