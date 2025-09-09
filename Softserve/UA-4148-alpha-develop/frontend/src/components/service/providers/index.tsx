import type { PropsWithChildren } from "react";
import { queryClient } from "./QueryClient";
import { QueryClientProvider } from "@tanstack/react-query";
import { AuthProvider } from "./AuthProvider";
import { WebSocketProvider } from "./WebSocket";

export function Providers({ children }: PropsWithChildren) {
  return (
    <AuthProvider>
      <WebSocketProvider>
        <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
      </WebSocketProvider>
    </AuthProvider>
  );
}
