import type { IStartup } from "@/components/composed_ui/StartupCard";
import axios from "./index";


export async function getStartups(): Promise<IStartup[]> {
  const response = await axios.get("/projects/");
  return response.data;
}
